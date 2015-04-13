# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0003_auto_20150412_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reel',
            name='link_default',
            field=models.CharField(help_text='Default target URL for reel images', max_length=255, null=True, verbose_name='Default Target', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reelimage',
            name='image',
            field=models.ImageField(height_field=b'height', upload_to=b'reel', width_field=b'width', verbose_name='Image'),
            preserve_default=True,
        ),
    ]
