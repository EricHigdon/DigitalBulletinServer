# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-25 03:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bulletin', '0012_auto_20161024_1928'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormSubmission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=5000)),
                ('church', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='form_submissions', to='bulletin.Church')),
            ],
        ),
    ]
