# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_auto_20150329_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='tracking_code',
            field=models.SlugField(max_length=10, null=True),
            preserve_default=True,
        ),
    ]
