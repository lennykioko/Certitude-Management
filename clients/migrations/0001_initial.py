# Generated by Django 2.1.3 on 2018-11-14 19:21

import clients.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordering', models.IntegerField(default=0)),
                ('joined', models.DateField(auto_now=True)),
                ('business', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(choices=[('POTENTIAL', 'POTENTIAL'), ('STALLED', 'STALLED'), ('IN_DISCUSSION', 'IN_DISCUSSION'), ('IN_PROGRESS', 'IN_PROGRESS'), ('COMPLETE', 'COMPLETE'), ('IN_UPSELL', 'IN_UPSELL')], max_length=255)),
                ('description', models.CharField(choices=[('DESKTOP_APPLICATION', 'DESKTOP_APPLICATION'), ('WEB_APPLICATION', 'WEB_APPLICATION'), ('WEBSITE', 'WEBSITE'), ('SOCIAL MEDIA MANAGEMENT', 'SOCIAL MEDIA MANAGEMENT'), ('TBD', 'TBD')], max_length=255)),
                ('stack', models.CharField(choices=[('NODE.JS/REACT/ELECTRON', 'NODE.JS/REACT/ELECTRON'), ('DJANGO', 'DJANGO'), ('DRF/REACT', 'DRF/REACT'), ('FLASK', 'FLASK'), ('N/A', 'N/A'), ('TBD', 'TBD'), ('REACT', 'REACT'), ('HTML/CSS/JS', 'HTML/CSS/JS')], max_length=255)),
                ('pivotal_tracker', models.URLField(blank=True, max_length=255, null=True)),
                ('repositories', models.TextField(blank=True, null=True)),
                ('dev_team', models.TextField(blank=True, null=True)),
                ('project_docs', models.TextField(blank=True, null=True)),
                ('total_amount', models.CharField(blank=True, max_length=255, null=True)),
                ('amount_paid', models.CharField(blank=True, max_length=255, null=True)),
                ('amount_due', models.CharField(blank=True, max_length=255, null=True)),
                ('expenditure', models.TextField(blank=True, null=True)),
                ('profit', models.TextField(blank=True, null=True)),
                ('expected_start_date', models.DateField(blank=True, null=True)),
                ('expected_duration', models.CharField(blank=True, max_length=255, null=True)),
                ('expected_end_date', models.DateField(blank=True, null=True)),
                ('actual_start_date', models.DateField(blank=True, null=True)),
                ('actual_end_date', models.DateField(blank=True, null=True)),
                ('actual_duration', models.CharField(blank=True, max_length=255, null=True)),
                ('product_urls', models.TextField(blank=True, null=True)),
                ('project_complexity', models.IntegerField(default=0, validators=[clients.models.validate_numbers])),
                ('rate_client', models.IntegerField(default=0, validators=[clients.models.validate_numbers])),
                ('comments', models.TextField(blank=True, null=True)),
                ('rating', models.IntegerField(default=0, validators=[clients.models.validate_numbers])),
                ('feedback', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ('ordering',),
            },
        ),
    ]