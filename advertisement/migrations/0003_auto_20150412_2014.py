# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0002_auto_20150409_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='target',
            field=models.CharField(help_text='If set, the banner becomes a link', max_length=255, null=True, verbose_name='Target', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reel',
            name='link_default',
            field=models.CharField(help_text='Default target URL for reel images', max_length=255, null=True, verbose_name='Default target', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reelimage',
            name='link_own',
            field=models.CharField(help_text='A reel image will become a link if it has a value in this field, or the owner reel has something in the default target field. If neither of those cases occur, the reel image will not be a link', max_length=255, null=True, verbose_name='Target', blank=True),
            preserve_default=True,
        ),
    ]
