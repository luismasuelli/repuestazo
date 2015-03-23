# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0002_auto_20150322_1927'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reelimage',
            options={'ordering': ('reel', 'sequence'), 'verbose_name': 'Reel image', 'verbose_name_plural': 'Reel images'},
        ),
        migrations.AddField(
            model_name='banner',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='banner',
            name='updated_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bannertype',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bannertype',
            name='updated_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='reel',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='reel',
            name='updated_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='reelimage',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='reelimage',
            name='updated_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='reeltype',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='reeltype',
            name='updated_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reelimage',
            name='sequence',
            field=models.PositiveIntegerField(verbose_name='Sequence', validators=[django.core.validators.MinValueValidator(1)]),
            preserve_default=True,
        ),
    ]
