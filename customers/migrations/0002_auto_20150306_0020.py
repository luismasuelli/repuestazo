# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone_number',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^09\\d{8}|0[2-8]\\d{7}$')]),
            preserve_default=True,
        ),
    ]
