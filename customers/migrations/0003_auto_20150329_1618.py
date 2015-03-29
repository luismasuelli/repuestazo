# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_auto_20150306_0020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contact',
            name='updated_on',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
            preserve_default=True,
        ),
    ]
