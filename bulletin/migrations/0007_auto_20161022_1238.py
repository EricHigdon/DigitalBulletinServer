# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-22 16:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bulletin', '0006_auto_20161022_1238'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='bulletin',
            new_name='church',
        ),
    ]
