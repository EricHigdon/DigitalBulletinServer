# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-23 05:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bulletin', '0010_auto_20161022_2210'),
    ]

    operations = [
        migrations.AddField(
            model_name='church',
            name='im_new',
            field=models.TextField(default=' ', max_length=10000),
            preserve_default=False,
        ),
    ]