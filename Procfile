release: python manage.py migrate && python manage.py setup_wagtail && python manage.py collectstatic --noinput
web: gunicorn sarkarinaukri.wsgi
