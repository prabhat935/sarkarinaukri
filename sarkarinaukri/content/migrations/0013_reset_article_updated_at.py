import datetime

from django.db import migrations


def reset_updated_at(apps, schema_editor):
    """Every deploy used to re-save all guides, so each one showed "Last
    updated" on the latest deploy date. Put each guide's date back to its
    publish date; guides whose text really changes are re-dated by the seed
    commands, which now save only on real changes."""
    Article = apps.get_model('content', 'Article')
    for article in Article.objects.all():
        published = datetime.datetime.combine(
            article.published_date, datetime.time(9, 0), tzinfo=datetime.timezone.utc
        )
        # .update() skips auto_now, so the stored date is the one we set
        Article.objects.filter(pk=article.pk).update(updated_at=published)


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0012_jobposting_location'),
    ]

    operations = [
        migrations.RunPython(reset_updated_at, migrations.RunPython.noop),
    ]
