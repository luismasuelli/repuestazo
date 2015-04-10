# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textsetelement',
            name='value',
            field=models.TextField(max_length=16777215, verbose_name='Content', blank=True),
            preserve_default=True,
        ),
    ]
