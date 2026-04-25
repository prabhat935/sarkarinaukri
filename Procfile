release: DJANGO_SETTINGS_MODULE=sarkarinaukri.settings.production python sarkarinaukri/manage.py migrate && DJANGO_SETTINGS_MODULE=sarkarinaukri.settings.production python sarkarinaukri/manage.py setup_wagtail && DJANGO_SETTINGS_MODULE=sarkarinaukri.settings.production python sarkarinaukri/manage.py collectstatic --noinput
web: gunicorn --chdir sarkarinaukri sarkarinaukri.wsgi --log-file -
