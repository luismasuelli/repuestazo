# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Replacement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('dealer', models.CharField(max_length=20)),
                ('score', models.CharField(max_length=1)),
                ('category', models.CharField(max_length=20)),
                ('code', models.CharField(max_length=20)),
                ('product', models.CharField(max_length=40)),
                ('brand', models.CharField(max_length=20)),
                ('model', models.CharField(max_length=255, blank=True)),
                ('year', models.SmallIntegerField(null=True, validators=[django.core.validators.MinValueValidator(2000)])),
                ('stock', models.DecimalField(null=True, max_digits=8, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)])),
                ('cost', models.DecimalField(null=True, max_digits=8, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)])),
                ('price', models.DecimalField(null=True, max_digits=8, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)])),
                ('offer', models.DecimalField(null=True, max_digits=8, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)])),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
