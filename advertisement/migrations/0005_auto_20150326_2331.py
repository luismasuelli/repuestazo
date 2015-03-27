# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0004_auto_20150325_2216'),
    ]

    operations = [
        migrations.CreateModel(
            name='RandomBanner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('code', models.SlugField(max_length=10, verbose_name='Code')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('description', models.CharField(max_length=100, verbose_name='Description')),
                ('banner_type', models.ForeignKey(verbose_name='Banner type', to='advertisement.BannerType')),
            ],
            options={
                'verbose_name': 'Random banner',
                'verbose_name_plural': 'Random banners',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RandomBannerChoice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('weight', models.PositiveIntegerField(verbose_name='Weight', validators=[django.core.validators.MinValueValidator(1)])),
                ('remaining_hits', models.PositiveIntegerField(null=True, verbose_name='Remaining hits')),
                ('banner', models.ForeignKey(verbose_name='Banner', to='advertisement.Banner')),
                ('owner', models.ForeignKey(related_name='choices', verbose_name='Random owner', to='advertisement.RandomBanner')),
            ],
            options={
                'verbose_name': 'Random banner',
                'verbose_name_plural': 'Random banners',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='randombannerchoice',
            unique_together=set([('owner', 'banner')]),
        ),
        migrations.AlterUniqueTogether(
            name='randombanner',
            unique_together=set([('code',)]),
        ),
    ]
