# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-22 16:27
from __future__ import unicode_literals

from django.conf import settings
import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Church',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=200)),
                ('modified_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('field_type', models.CharField(choices=[('char', 'Text'), ('email', 'Email'), ('phone', 'Phone'), ('text', 'Long Text'), ('int', 'Number'), ('bool', 'Checkbox'), ('choice', 'Choice'), ('file', 'File')], max_length=200)),
                ('required', models.BooleanField()),
                ('sort_order', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('recipient', models.CharField(help_text='a comma separated list of emails', max_length=500)),
                ('church', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='forms', to='bulletin.Church')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.FileField(blank=True, storage=django.core.files.storage.FileSystemStorage(location='/Users/erichigdon/venvs/churchapp/lib/python3.5/site-packages/django/contrib/admin/static/img/uploads/'), upload_to='')),
                ('content', models.TextField(max_length=5000)),
                ('sort_order', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('template', models.TextField(max_length=5000)),
                ('church', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pages', to='bulletin.Church')),
            ],
        ),
        migrations.CreateModel(
            name='Passage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.CharField(choices=[('gen', 'Genesis'), ('ex', 'Exodus'), ('lev', 'Leviticus'), ('num', 'Numbers'), ('deu', 'Deuteronomy'), ('joshua', 'Joshua'), ('judges', 'Judges'), ('ruth', 'Ruth'), ('1samuel', '1 Samuel'), ('2samuel', '2 Samuel'), ('1kings', '1 Kings'), ('2kings', '2 Kings'), ('1chronicles', '1 Chronicles'), ('2chronicles', '2 Chronicles'), ('ezra', 'Ezra'), ('nehimiah', 'Nehemiah'), ('esther', 'Esther'), ('job', 'Job'), ('psalms', 'Psalms'), ('proverbs', 'Proverbs'), ('ecclesiastes', 'Ecclesiastes'), ('songofsolomon', 'Song of Solomon'), ('isaiah', 'Isaiah'), ('jeremiah', 'Jeremiah'), ('lamentations', 'Lamentations'), ('ezekiel', 'Ezekiel'), ('daniel', 'Daniel'), ('hosea', 'Hosea'), ('joel', 'Joel'), ('amos', 'Amos'), ('obadiah', 'Obadiah'), ('jonah', 'Jonah'), ('micah', 'Micah'), ('nahum', 'Nahum'), ('habakkuk', 'Habakkuk'), ('zephaniah', 'Zephaniah'), ('haggai', 'Haggai'), ('zechariah', 'Zechariah'), ('malachi', 'Malachi'), ('matthew', 'Matthew'), ('mark', 'Mark'), ('luke', 'Luke'), ('john', 'John'), ('acts', 'Acts'), ('romans', 'Romans'), ('1corinthians', '1 Corinthians'), ('2corinthians', '2 Corinthians'), ('galatians', 'Galatians'), ('ephesians', 'Ephesians'), ('philippians', 'Philippians'), ('colossians', 'Colossians'), ('1thessalonians', '1 Thessalonians'), ('2thessalonians', '2 Thessalonians'), ('1timothy', '1 Timothy'), ('2timothy', '2 Timothy'), ('titus', 'Titus'), ('philemon', 'Philemon'), ('hebrews', 'Hebrews'), ('james', 'James'), ('1peter', '1 Peter'), ('2peter', '2 Peter'), ('1john', '1 John'), ('2john', '2 John'), ('3john', '3 John'), ('jude', 'Jude'), ('revelation', 'Revelation')], max_length=200)),
                ('chapter', models.IntegerField(blank=True, null=True)),
                ('verse', models.CharField(blank=True, max_length=200)),
                ('church', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='passages', to='bulletin.Church')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='bulletin.Page'),
        ),
        migrations.AddField(
            model_name='field',
            name='form',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fields', to='bulletin.Form'),
        ),
        migrations.AddField(
            model_name='choice',
            name='field',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='bulletin.Field'),
        ),
    ]