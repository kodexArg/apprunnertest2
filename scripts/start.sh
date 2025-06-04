#!/bin/bash
set -e

# Install uv if not present
pip3 install uv

# Debug output for SECRET_KEY
echo "DEBUG: SECRET_KEY is set to: ${SECRET_KEY}"

# Run Django migrations
.venv/bin/python manage.py makemigrations
.venv/bin/python manage.py migrate

# Create superuser
.venv/bin/python manage.py createsuperuser --noinput

# Start Gunicorn
exec .venv/bin/gunicorn -b 0.0.0.0:8080 project.wsgi 