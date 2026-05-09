#!/bin/bash
set -e

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$REPO_ROOT/sarkarinaukri"

export DJANGO_SETTINGS_MODULE=sarkarinaukri.settings.production

echo "==> Collecting static files..."
python manage.py collectstatic --noinput --clear

echo "==> Running migrations..."
python manage.py migrate

echo "==> Seeding SarkariResult data..."
python manage.py add_sarkariresult_data

echo "==> Running daily SEO update..."
python manage.py daily_seo_update

echo "==> Starting gunicorn..."
exec gunicorn sarkarinaukri.wsgi --log-file -
