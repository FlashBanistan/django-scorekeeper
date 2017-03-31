# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-31 03:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books_and_run', '0004_auto_20170306_0922'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='players',
        ),
        migrations.RemoveField(
            model_name='game',
            name='winner',
        ),
        migrations.AlterUniqueTogether(
            name='score',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='score',
            name='game',
        ),
        migrations.RemoveField(
            model_name='score',
            name='player',
        ),
        migrations.AlterModelOptions(
            name='statistics',
            options={'verbose_name_plural': 'statistics'},
        ),
        migrations.DeleteModel(
            name='Game',
        ),
        migrations.DeleteModel(
            name='Score',
        ),
    ]
