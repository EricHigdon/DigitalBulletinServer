# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-19 02:09
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('image', models.FileField(blank=True, storage=django.core.files.storage.FileSystemStorage(location='/home3/ehigdon/public_html/static/accord/img/uploads'), upload_to='')),
            ],
        ),
    ]