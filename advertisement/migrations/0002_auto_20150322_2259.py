# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='target',
            field=models.URLField(help_text='If set, the banner becomes a link', null=True, verbose_name='Target', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='reel',
            name='link_default',
            field=models.URLField(help_text='Default target URL for reel images', null=True, verbose_name='Default target', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='reel',
            name='link_prevails',
            field=models.BooleanField(default=False, help_text="Tells whether clicking any reel image will always make use of the default target instead of following the image's critera. Such criterion is only effective when the default target is set", verbose_name='Prevailing target'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='reelimage',
            name='link_own',
            field=models.URLField(help_text='A reel image will become a link if it has a value in this field, or the owner reel has something in the default target field. If neither of those cases occur, the reel image will not be a link', null=True, verbose_name='Target', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reelimage',
            name='image',
            field=models.ImageField(height_field=b'height', width_field=b'width', upload_to=b'reel'),
            preserve_default=True,
        ),
    ]
