# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-22 16:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bulletin', '0004_auto_20161022_1235'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='church',
            name='date',
        ),
        migrations.AddField(
            model_name='church',
            name='modified_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
