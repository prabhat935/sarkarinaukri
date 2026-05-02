release: DJANGO_SETTINGS_MODULE=sarkarinaukri.settings.production python sarkarinaukri/manage.py collectstatic --noinput && DJANGO_SETTINGS_MODULE=sarkarinaukri.settings.production python sarkarinaukri/manage.py migrate
web: gunicorn --chdir sarkarinaukri sarkarinaukri.wsgi --log-file -
