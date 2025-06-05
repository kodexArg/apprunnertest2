#!/bin/bash

set -e  # Detener el script si hay algún error

echo "Ejecutando migraciones de Django..."
.venv/bin/python manage.py makemigrations
.venv/bin/python manage.py migrate

echo "Recolectando archivos estáticos..."
.venv/bin/python manage.py collectstatic --noinput

echo "Verificando existencia de superusuario..."
if ! .venv/bin/python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); print(User.objects.filter(is_superuser=True).exists())" | grep -q "True"; then
    echo "Creando superusuario..."
    .venv/bin/python manage.py createsuperuser --noinput
else
    echo "Superusuario ya existe, omitiendo creación."
fi

echo "Ejecutando tests de configuración..."
.venv/bin/python manage.py test core.tests.test_config --verbosity 2
if [ $? -ne 0 ]; then
    echo "Los tests han fallado. Abortando despliegue."
    exit 1
fi
echo "Tests completados exitosamente."

echo "Iniciando servidor Gunicorn..."
exec .venv/bin/gunicorn -b 0.0.0.0:8080 project.wsgi --log-level info --access-logfile - --error-logfile - 