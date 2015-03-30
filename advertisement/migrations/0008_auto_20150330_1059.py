# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0007_auto_20150329_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='randombannerchoice',
            name='remaining_hits',
            field=models.PositiveIntegerField(null=True, verbose_name='Remaining hits', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='randomtextsetchoice',
            name='remaining_hits',
            field=models.PositiveIntegerField(null=True, verbose_name='Remaining hits', blank=True),
            preserve_default=True,
        ),
    ]
