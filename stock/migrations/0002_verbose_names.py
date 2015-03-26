# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='replacement',
            options={'verbose_name': 'Replacement', 'verbose_name_plural': 'Replacements'},
        ),
        migrations.AlterField(
            model_name='replacement',
            name='brand',
            field=models.CharField(max_length=20, verbose_name='Brand'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='replacement',
            name='category',
            field=models.CharField(max_length=20, verbose_name='Category'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='replacement',
            name='code',
            field=models.CharField(max_length=20, verbose_name='Code'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='replacement',
            name='cost',
            field=models.DecimalField(null=True, verbose_name='Cost', max_digits=8, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='replacement',
            name='dealer',
            field=models.CharField(max_length=20, verbose_name='Dealer'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='replacement',
            name='model',
            field=models.CharField(max_length=255, verbose_name='Model', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='replacement',
            name='offer',
            field=models.DecimalField(null=True, verbose_name='Offer', max_digits=8, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='replacement',
            name='price',
            field=models.DecimalField(null=True, verbose_name='Price', max_digits=8, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='replacement',
            name='product',
            field=models.CharField(max_length=40, verbose_name='Product'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='replacement',
            name='score',
            field=models.CharField(max_length=1, verbose_name='Score'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='replacement',
            name='stock',
            field=models.DecimalField(null=True, verbose_name='Stock', max_digits=8, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='replacement',
            name='year',
            field=models.SmallIntegerField(null=True, verbose_name='Year', validators=[django.core.validators.MinValueValidator(2000)]),
            preserve_default=True,
        ),
    ]
