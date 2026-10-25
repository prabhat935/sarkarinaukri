from django.db import migrations, models


OLD = {
    'author_name': 'Sarkari Naukri Editor',
    'author_credentials': 'Career Counselor, Government Job Expert',
    'author_bio': 'Specialist in government job guidance with 8+ years of experience',
}
NEW = {
    'author_name': 'Sarkari Naukri Editorial Team',
    'author_credentials': 'Checked against official notifications',
    'author_bio': 'Written and reviewed by the Sarkari Naukri editorial team.',
}


def use_team_byline(apps, schema_editor):
    Article = apps.get_model('content', 'Article')
    for field, old in OLD.items():
        Article.objects.filter(**{field: old}).update(**{field: NEW[field]})


def restore_old_byline(apps, schema_editor):
    Article = apps.get_model('content', 'Article')
    for field, new in NEW.items():
        Article.objects.filter(**{field: new}).update(**{field: OLD[field]})


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0010_article_author_bio_article_author_credentials_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author_bio',
            field=models.CharField(default='Written and reviewed by the Sarkari Naukri editorial team.', help_text='Author bio for byline', max_length=300),
        ),
        migrations.AlterField(
            model_name='article',
            name='author_credentials',
            field=models.CharField(default='Checked against official notifications', help_text='Author expertise/credentials', max_length=150),
        ),
        migrations.AlterField(
            model_name='article',
            name='author_name',
            field=models.CharField(default='Sarkari Naukri Editorial Team', help_text='Author name for byline', max_length=100),
        ),
        migrations.RunPython(use_team_byline, restore_old_byline),
    ]
