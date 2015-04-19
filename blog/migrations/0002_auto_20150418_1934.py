# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='entry',
            options={'verbose_name': 'Entry', 'verbose_name_plural': 'Entries'},
        ),
        migrations.AlterField(
            model_name='category',
            name='code',
            field=models.SlugField(unique=True, max_length=20, verbose_name='Code', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='entry',
            name='slug',
            field=models.CharField(max_length=50, verbose_name='Slug', blank=True),
            preserve_default=True,
        ),
    ]
