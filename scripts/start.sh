#!/bin/bash

set -e  # Stop script if any error occurs

# --- Eliminar base de datos de test si existe ---
echo "Checking and dropping test database if exists..."
export PGPASSWORD="$DB_PASSWORD"
psql -h "$DB_HOST" -U "$DB_USERNAME" -p "$DB_PORT" -d postgres -c "DROP DATABASE IF EXISTS test_$DB_NAME;" || true
unset PGPASSWORD

echo "Running Django migrations..."
.venv/bin/python manage.py makemigrations
.venv/bin/python manage.py migrate

echo "Collecting static files..."
.venv/bin/python manage.py collectstatic --noinput

echo "Checking superuser existence..."
if ! .venv/bin/python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); print(User.objects.filter(is_superuser=True).exists())" | grep -q "True"; then
    echo "Creating superuser..."
    .venv/bin/python manage.py createsuperuser --noinput
else
    echo "Superuser already exists, skipping creation."
fi

echo "Running tests in order..."

echo "1. Running configuration tests..."
.venv/bin/python manage.py test tests.test_config --verbosity 2
if [ $? -ne 0 ]; then
    echo "Configuration tests failed. Aborting deployment."
    exit 1
fi
echo "Configuration tests passed."

echo "2. Running startup tests..."
.venv/bin/python manage.py test tests.test_startup --verbosity 2
if [ $? -ne 0 ]; then
    echo "Startup tests failed. Aborting deployment."
    exit 1
fi
echo "Startup tests passed."

echo "3. Running integration tests..."
.venv/bin/python manage.py test tests.test_integration --verbosity 2
if [ $? -ne 0 ]; then
    echo "Integration tests failed. Aborting deployment."
    exit 1
fi
echo "Integration tests passed."

echo "4. Running application tests..."
echo "4.1. Running core.views tests..."
.venv/bin/python manage.py test core.tests.test_views --verbosity 2
if [ $? -ne 0 ]; then
    echo "core.views tests failed. Aborting deployment."
    exit 1
fi

echo "4.2. Running core.models tests..."
.venv/bin/python manage.py test core.tests.test_models --verbosity 2
if [ $? -ne 0 ]; then
    echo "core.models tests failed. Aborting deployment."
    exit 1
fi

echo "All application tests passed successfully."

echo "Starting Gunicorn server..."
exec .venv/bin/gunicorn -b 0.0.0.0:8080 project.wsgi --log-level info --access-logfile - --error-logfile - 