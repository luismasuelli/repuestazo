# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0003_auto_20150329_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='replacement',
            name='cost',
            field=models.DecimalField(decimal_places=2, validators=[django.core.validators.MinValueValidator(0)], max_digits=8, blank=True, null=True, verbose_name='Cost'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='replacement',
            name='offer',
            field=models.DecimalField(decimal_places=2, validators=[django.core.validators.MinValueValidator(0)], max_digits=8, blank=True, null=True, verbose_name='Offer'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='replacement',
            name='price',
            field=models.DecimalField(decimal_places=2, validators=[django.core.validators.MinValueValidator(0)], max_digits=8, blank=True, null=True, verbose_name='Price'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='replacement',
            name='stock',
            field=models.DecimalField(decimal_places=2, validators=[django.core.validators.MinValueValidator(0)], max_digits=8, blank=True, null=True, verbose_name='Stock'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='replacement',
            name='year',
            field=models.SmallIntegerField(blank=True, null=True, verbose_name='Year', validators=[django.core.validators.MinValueValidator(2000)]),
            preserve_default=True,
        ),
    ]
