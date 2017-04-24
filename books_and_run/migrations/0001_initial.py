# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-24 12:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Statistics',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('games_won', models.IntegerField(default=0)),
                ('hands_won', models.IntegerField(default=0)),
                ('games_played', models.IntegerField(default=0)),
                ('high_score', models.IntegerField(blank=True, null=True)),
                ('low_score', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'statistics',
            },
        ),
    ]
