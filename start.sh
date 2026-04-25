#!/bin/bash
set -e

cd sarkarinaukri

python manage.py migrate --fake-initial
python manage.py setup_wagtail
python manage.py collectstatic --noinput

gunicorn sarkarinaukri.wsgi --log-file -
