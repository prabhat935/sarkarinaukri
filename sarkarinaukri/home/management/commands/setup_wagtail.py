import os

from django.core.management.base import BaseCommand
from django.contrib.contenttypes.models import ContentType


class Command(BaseCommand):
    help = "Creates the initial Wagtail Site and HomePage if they do not exist"

    def handle(self, *args, **options):
        from wagtail.models import Page, Site
        from home.models import HomePage

        # Determine hostname from Railway env var, falling back to localhost
        hostname = os.environ.get("RAILWAY_PUBLIC_DOMAIN", "localhost")
        port = 443 if os.environ.get("RAILWAY_PUBLIC_DOMAIN") else 80

        # Check whether a Site already exists — if so, nothing to do
        if Site.objects.exists():
            self.stdout.write(
                self.style.SUCCESS("Wagtail site already exists — skipping setup.")
            )
            return

        # ------------------------------------------------------------------
        # Ensure a HomePage exists
        # ------------------------------------------------------------------
        homepage = HomePage.objects.filter(slug="home", depth=2).first()

        if homepage is None:
            self.stdout.write("Creating HomePage…")

            homepage_content_type, _ = ContentType.objects.get_or_create(
                model="homepage", app_label="home"
            )

            # The Wagtail page tree requires a root node at depth=1 (path "0001").
            # Wagtail's initial migrations create this root, but guard against it
            # being absent just in case.
            root_page = Page.objects.filter(depth=1).first()
            if root_page is None:
                self.stderr.write(
                    self.style.ERROR(
                        "No root page found in the Wagtail page tree. "
                        "Ensure migrations have been applied correctly."
                    )
                )
                return

            homepage = HomePage(
                title="Home",
                draft_title="Home",
                slug="home",
                content_type=homepage_content_type,
                path="00010001",
                depth=2,
                numchild=0,
                url_path="/home/",
            )
            root_page.add_child(instance=homepage)
            self.stdout.write(self.style.SUCCESS("HomePage created."))
        else:
            self.stdout.write("HomePage already exists — skipping creation.")

        # ------------------------------------------------------------------
        # Create the Wagtail Site pointing at the HomePage
        # ------------------------------------------------------------------
        self.stdout.write(f"Creating Wagtail site for hostname '{hostname}'…")
        Site.objects.create(
            hostname=hostname,
            port=port,
            root_page=homepage,
            is_default_site=True,
        )
        self.stdout.write(
            self.style.SUCCESS(
                f"Wagtail site created: {hostname}:{port} → HomePage (pk={homepage.pk})"
            )
        )
