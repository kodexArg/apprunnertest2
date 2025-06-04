#!/bin/bash
set -e

# Install uv if not present
pip3 install uv

# Debug output for SECRET_KEY
echo "DEBUG: SECRET_KEY is set to: ${SECRET_KEY}"

# Run Django migrations
.venv/bin/python manage.py makemigrations
.venv/bin/python manage.py migrate

# Check if superuser exists and create if not
if ! .venv/bin/python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); print(User.objects.filter(is_superuser=True).exists())" | grep -q "True"; then
    echo "Creating superuser..."
    .venv/bin/python manage.py createsuperuser --noinput
else
    echo "Superuser already exists, skipping creation."
fi

# Start Gunicorn
exec .venv/bin/gunicorn -b 0.0.0.0:8080 project.wsgi 