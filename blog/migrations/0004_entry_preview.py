# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_monthentriesbreakdown'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='preview',
            field=models.TextField(default='', verbose_name='Preview'),
            preserve_default=False,
        ),
    ]
