# Generated migration for expanded models

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('content', '0001_initial'),
    ]

    operations = [
        # Create reference models
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, unique=True)),
                ('slug', models.SlugField(db_index=True, unique=True)),
                ('description', models.TextField(blank=True)),
                ('website', models.URLField(blank=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='org_logos/')),
                ('is_featured', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Organizations',
                'ordering': ['-is_featured', 'name'],
            },
        ),
        migrations.CreateModel(
            name='ExamCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, unique=True)),
                ('slug', models.SlugField(db_index=True, unique=True)),
                ('description', models.TextField(blank=True)),
                ('icon', models.CharField(blank=True, max_length=50)),
                ('is_featured', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Exam Categories',
                'ordering': ['-is_featured', 'name'],
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50, unique=True)),
                ('code', models.CharField(max_length=2, unique=True)),
                ('is_featured', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-is_featured', 'name'],
            },
        ),
        migrations.CreateModel(
            name='QualificationLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(choices=[('10th', '10th Pass'), ('12th', '12th Pass'), ('graduate', 'Graduate'), ('pg', 'Post Graduate'), ('phd', 'Ph.D')], max_length=20, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Qualification Levels',
            },
        ),
        # Add fields to JobPosting
        migrations.AddField(
            model_name='jobposting',
            name='slug',
            field=models.SlugField(default='', db_index=True, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobposting',
            name='job_level',
            field=models.CharField(blank=True, choices=[('A', 'Group A'), ('B', 'Group B'), ('C', 'Group C'), ('D', 'Group D')], db_index=True, max_length=20),
        ),
        migrations.AddField(
            model_name='jobposting',
            name='min_age',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='jobposting',
            name='max_age',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='jobposting',
            name='salary_min',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='jobposting',
            name='salary_max',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='jobposting',
            name='experience_required',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='jobposting',
            name='gender_preference',
            field=models.CharField(choices=[('Any', 'Any'), ('Male', 'Male Only'), ('Female', 'Female Only')], default='Any', max_length=20),
        ),
        migrations.AddField(
            model_name='jobposting',
            name='interview_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='jobposting',
            name='result_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='jobposting',
            name='application_fee',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='jobposting',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Closed', 'Closed'), ('Postponed', 'Postponed'), ('Cancelled', 'Cancelled')], db_index=True, default='Active', max_length=20),
        ),
        migrations.AddField(
            model_name='jobposting',
            name='meta_description',
            field=models.CharField(blank=True, help_text='Google meta description', max_length=160),
        ),
        migrations.AddField(
            model_name='jobposting',
            name='meta_keywords',
            field=models.CharField(blank=True, max_length=160),
        ),
        # Remove old char fields and add ForeignKey fields
        migrations.RemoveField(
            model_name='jobposting',
            name='organization',
        ),
        migrations.RemoveField(
            model_name='jobposting',
            name='state',
        ),
        migrations.RemoveField(
            model_name='jobposting',
            name='category',
        ),
        migrations.AddField(
            model_name='jobposting',
            name='organization',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='content.organization'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobposting',
            name='exam_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='content.examcategory'),
        ),
        migrations.AddField(
            model_name='jobposting',
            name='state',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='content.state'),
        ),
        migrations.AddField(
            model_name='jobposting',
            name='qualification_level',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='content.qualificationlevel'),
        ),
        # Update JobPosting indexes
        migrations.AddIndex(
            model_name='jobposting',
            index=models.Index(fields=['state', '-created_at'], name='content_job_state_created_idx'),
        ),
        migrations.AddIndex(
            model_name='jobposting',
            index=models.Index(fields=['organization', '-created_at'], name='content_job_org_created_idx'),
        ),
        migrations.AddIndex(
            model_name='jobposting',
            index=models.Index(fields=['exam_category', '-created_at'], name='content_job_cat_created_idx'),
        ),
        # Update ExamResult
        migrations.AddField(
            model_name='examresult',
            name='slug',
            field=models.SlugField(default='', db_index=True, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='examresult',
            name='exam_year',
            field=models.IntegerField(db_index=True, default=2026),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='examresult',
            name='result_pdf_link',
            field=models.URLField(blank=True, help_text='Direct link to result PDF'),
        ),
        migrations.AddField(
            model_name='examresult',
            name='merit_list_link',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='examresult',
            name='cutoff_marks_link',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='examresult',
            name='total_posts',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='examresult',
            name='selected_candidates',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='examresult',
            name='is_official',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='examresult',
            name='meta_description',
            field=models.CharField(blank=True, max_length=160),
        ),
        migrations.RemoveField(
            model_name='examresult',
            name='merit_list',
        ),
        migrations.RemoveField(
            model_name='examresult',
            name='state',
        ),
        migrations.RemoveField(
            model_name='examresult',
            name='category',
        ),
        migrations.AddField(
            model_name='examresult',
            name='organization',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='content.organization'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='examresult',
            name='exam_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='content.examcategory'),
        ),
        migrations.AddField(
            model_name='examresult',
            name='state',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='content.state'),
        ),
        migrations.AddField(
            model_name='examresult',
            name='exam_name',
            field=models.CharField(db_index=True, default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='examresult',
            unique_together={('exam_name', 'exam_year')},
        ),
        # Update AdmitCard
        migrations.AddField(
            model_name='admitcard',
            name='slug',
            field=models.SlugField(default='', db_index=True, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='admitcard',
            name='exam_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='admitcard',
            name='exam_duration',
            field=models.CharField(blank=True, help_text='e.g., 2 hours', max_length=20),
        ),
        migrations.AddField(
            model_name='admitcard',
            name='instructions',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='admitcard',
            name='admit_card_date',
            field=models.DateField(default='2026-04-22'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='admitcard',
            name='state',
        ),
        migrations.RemoveField(
            model_name='admitcard',
            name='category',
        ),
        migrations.AddField(
            model_name='admitcard',
            name='organization',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='content.organization'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='admitcard',
            name='exam_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='content.examcategory'),
        ),
        migrations.AddField(
            model_name='admitcard',
            name='state',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='content.state'),
        ),
        migrations.AddField(
            model_name='admitcard',
            name='exam_name',
            field=models.CharField(db_index=True, default='', max_length=200),
            preserve_default=False,
        ),
        # Update Syllabus
        migrations.AddField(
            model_name='syllabus',
            name='slug',
            field=models.SlugField(default='', db_index=True, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='syllabus',
            name='exam_year',
            field=models.IntegerField(default=2026),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='syllabus',
            name='subjects',
            field=models.TextField(default='', help_text='Comma-separated list of subjects'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='syllabus',
            name='detailed_syllabus_link',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='syllabus',
            name='important_topics',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='syllabus',
            name='previous_papers_link',
            field=models.URLField(blank=True),
        ),
        migrations.RemoveField(
            model_name='syllabus',
            name='state',
        ),
        migrations.RemoveField(
            model_name='syllabus',
            name='category',
        ),
        migrations.AddField(
            model_name='syllabus',
            name='organization',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='content.organization'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='syllabus',
            name='exam_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='content.examcategory'),
        ),
        migrations.AddField(
            model_name='syllabus',
            name='state',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='content.state'),
        ),
        migrations.AddField(
            model_name='syllabus',
            name='exam_name',
            field=models.CharField(db_index=True, default='', max_length=200),
            preserve_default=False,
        ),
        # Create new models
        migrations.CreateModel(
            name='AnswerKey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(db_index=True)),
                ('description', models.TextField(blank=True)),
                ('exam_year', models.IntegerField(db_index=True)),
                ('exam_date', models.DateField()),
                ('publication_date', models.DateField(auto_now_add=True)),
                ('shift_number', models.PositiveIntegerField(default=1, help_text='For multiple shifts')),
                ('question_paper_link', models.URLField(blank=True)),
                ('answer_key_link', models.URLField()),
                ('solution_pdf_link', models.URLField(blank=True)),
                ('is_official', models.BooleanField(default=False)),
                ('is_provisional', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('exam_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='content.examcategory')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='content.organization')),
                ('state', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='content.state')),
            ],
            options={
                'ordering': ['-exam_date'],
                'unique_together': {('exam_name', 'exam_year', 'shift_number')},
            },
        ),
        migrations.CreateModel(
            name='AdmissionForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('institution_name', models.CharField(max_length=200)),
                ('form_start_date', models.DateField()),
                ('form_end_date', models.DateField()),
                ('merit_list_date', models.DateField(blank=True, null=True)),
                ('counselling_date', models.DateField(blank=True, null=True)),
                ('form_link', models.URLField()),
                ('application_fee', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('eligibility', models.TextField(blank=True)),
                ('status', models.CharField(choices=[('Open', 'Open'), ('Closed', 'Closed'), ('Postponed', 'Postponed')], default='Open', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('exam_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='content.examcategory')),
                ('state', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='content.state')),
            ],
            options={
                'ordering': ['-form_start_date'],
            },
        ),
        migrations.CreateModel(
            name='CertificateVerification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_name', models.CharField(db_index=True, max_length=200, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('verification_link', models.URLField()),
                ('year', models.IntegerField(blank=True, null=True)),
                ('instructions', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('exam_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='content.examcategory')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='content.organization')),
            ],
        ),
        migrations.CreateModel(
            name='SavedJob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saved_at', models.DateTimeField(auto_now_add=True)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.jobposting')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='saved_jobs', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Saved Jobs',
                'unique_together': {('user', 'job')},
            },
        ),
    ]
