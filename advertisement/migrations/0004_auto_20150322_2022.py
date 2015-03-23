# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0003_auto_20150322_2005'),
    ]

    operations = [
        migrations.AddField(
            model_name='reelimage',
            name='height',
            field=models.PositiveIntegerField(default=0, verbose_name='Reel image height', editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reelimage',
            name='image',
            field=models.ImageField(default=None, height_field=b'height', width_field=b'width', upload_to=b'reel'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reelimage',
            name='width',
            field=models.PositiveIntegerField(default=0, verbose_name='Reel image width', editable=False),
            preserve_default=False,
        ),
    ]
