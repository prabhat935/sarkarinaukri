from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command
from django.contrib.auth.models import User
from wagtail.models import Site, Page
from home.models import HomePage
import os

class Command(BaseCommand):
    help = 'Setup Wagtail CMS with initial data and superuser'

    def handle(self, *args, **options):
        self.stdout.write('🚀 Setting up Wagtail CMS...')

        try:
            # Import initial data
            self.stdout.write('📥 Importing initial reference data...')
            call_command('import_initial_data')
            self.stdout.write(self.style.SUCCESS('✓ Initial data imported'))
        except Exception as e:
            raise CommandError(f'Failed to import initial data: {e}') from e

        # Skip sample data population in production to avoid deployment timeouts
        if os.environ.get('SKIP_SAMPLE_DATA') != 'true':
            try:
                # Populate sample data
                self.stdout.write('📊 Populating sample data...')
                call_command('populate_data')
                self.stdout.write(self.style.SUCCESS('✓ Sample data populated'))
            except Exception as e:
                raise CommandError(f'Failed to populate data: {e}') from e
        else:
            self.stdout.write('📊 Skipping sample data population (SKIP_SAMPLE_DATA=true)')

        try:
            # Create superuser if it doesn't exist
            if not User.objects.filter(is_superuser=True).exists():
                self.stdout.write('👤 Creating superuser...')
                User.objects.create_superuser(
                    username='admin',
                    email='admin@example.com',
                    password='admin123'
                )
                self.stdout.write(self.style.SUCCESS('✓ Superuser created: admin/admin123'))
            else:
                self.stdout.write('👤 Superuser already exists, skipping...')
        except Exception as e:
            raise CommandError(f'Failed to create superuser: {e}') from e

        try:
            # Ensure homepage exists
            if not HomePage.objects.exists():
                self.stdout.write('🏠 Creating homepage...')
                # Get the root page (should exist after Wagtail migrations)
                try:
                    root_page = Page.objects.get(depth=1)
                except Page.DoesNotExist:
                    raise CommandError(
                        'Root page not found. Wagtail may not be properly initialized. '
                        'Ensure wagtail migrations have been applied.'
                    )

                homepage = HomePage(
                    title='Sarkari Naukri',
                    slug='home'
                )
                root_page.add_child(instance=homepage)
                # Publish the homepage
                homepage.save_revision().publish()
                self.stdout.write(self.style.SUCCESS('✓ Homepage created and published'))
            else:
                self.stdout.write('🏠 Homepage already exists, skipping...')
        except CommandError:
            raise
        except Exception as e:
            raise CommandError(f'Failed to create homepage: {e}') from e

        try:
            # Update site settings
            self.stdout.write('⚙️ Updating site settings...')
            site = Site.objects.get(is_default_site=True)
            site.site_name = 'Sarkari Naukri'
            # Set the root page to the homepage
            homepage = HomePage.objects.first()
            if homepage:
                site.root_page = homepage
                site.save()
            self.stdout.write(self.style.SUCCESS('✓ Site settings updated'))
        except Site.DoesNotExist:
            self.stdout.write(self.style.WARNING('⚠️  Default site not found, skipping site settings update'))
        except Exception as e:
            raise CommandError(f'Failed to update site settings: {e}') from e

        self.stdout.write(self.style.SUCCESS('✅ Wagtail setup complete!'))