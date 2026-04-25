release: python sarkarinaukri/manage.py migrate && python sarkarinaukri/manage.py setup_wagtail && python sarkarinaukri/manage.py collectstatic --noinput
web: gunicorn --chdir sarkarinaukri sarkarinaukri.wsgi --log-file -
