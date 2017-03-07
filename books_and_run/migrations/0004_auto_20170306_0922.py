# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-06 16:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books_and_run', '0003_statistics'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='statistics',
            name='id',
        ),
        migrations.AlterField(
            model_name='statistics',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
