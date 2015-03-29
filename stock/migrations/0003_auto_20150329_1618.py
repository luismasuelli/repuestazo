# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_verbose_names'),
    ]

    operations = [
        migrations.AlterField(
            model_name='replacement',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='replacement',
            name='updated_on',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
            preserve_default=True,
        ),
    ]
