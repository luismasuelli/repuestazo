# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.SlugField(unique=True, max_length=20, verbose_name='Code')),
                ('name', models.CharField(max_length=40, verbose_name='Name')),
                ('description', models.CharField(max_length=255, verbose_name='Description')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_on', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('slug', models.CharField(max_length=50, verbose_name='Slug')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('content', tinymce.models.HTMLField(max_length=16777215, verbose_name='Content')),
                ('category', models.ForeignKey(to='blog.Category')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
