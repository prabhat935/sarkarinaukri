#!/bin/bash
set -e

cd sarkarinaukri

export DJANGO_SETTINGS_MODULE=sarkarinaukri.settings.production

echo "==> Collecting static files..."
python manage.py collectstatic --noinput --clear

echo "==> Running migrations..."
python manage.py migrate

echo "==> Starting gunicorn..."
exec gunicorn sarkarinaukri.wsgi --log-file -
