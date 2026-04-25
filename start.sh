#!/bin/bash
set -e

cd sarkarinaukri

python manage.py migrate --run-syncdb
python manage.py setup_wagtail
python manage.py collectstatic --noinput

gunicorn sarkarinaukri.wsgi --log-file -
