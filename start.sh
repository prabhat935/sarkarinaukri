#!/bin/bash
set -e

cd sarkarinaukri

DJANGO_SETTINGS_MODULE=sarkarinaukri.settings.production python manage.py migrate --run-syncdb
DJANGO_SETTINGS_MODULE=sarkarinaukri.settings.production python manage.py setup_wagtail
rm -f static/staticfiles.json
DJANGO_SETTINGS_MODULE=sarkarinaukri.settings.production python manage.py collectstatic --noinput

gunicorn sarkarinaukri.wsgi --log-file -
