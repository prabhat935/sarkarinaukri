from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0007_alter_admitcard_exam_name_alter_examresult_exam_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('excerpt', models.CharField(max_length=300)),
                ('content', models.TextField()),
                ('category', models.CharField(
                    choices=[
                        ('exam-guide', 'Exam Guide'),
                        ('preparation', 'Preparation Tips'),
                        ('career', 'Career Advice'),
                        ('news', 'News & Updates'),
                    ],
                    db_index=True,
                    default='exam-guide',
                    max_length=20,
                )),
                ('published_date', models.DateField(db_index=True)),
                ('meta_description', models.CharField(blank=True, max_length=160)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-published_date'],
            },
        ),
    ]
