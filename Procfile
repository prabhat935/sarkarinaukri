release: python manage.py migrate && python manage.py setup_wagtail
web: cd sarkarinaukri && python manage.py collectstatic --noinput && gunicorn sarkarinaukri.wsgi
