#!/usr/bin/env python
"""Root-level shim so Railway/Railpack can find manage.py at /app/manage.py."""
import os
import sys

if __name__ == '__main__':
    project_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sarkarinaukri')
    os.chdir(project_dir)
    sys.path.insert(0, project_dir)
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sarkarinaukri.settings.production')
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
