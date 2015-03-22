# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.SlugField(max_length=10, verbose_name='Code')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('description', models.CharField(max_length=100, verbose_name='Description')),
                ('width', models.PositiveIntegerField(verbose_name='Banner width', editable=False)),
                ('height', models.PositiveIntegerField(verbose_name='Banner height', editable=False)),
                ('image', models.ImageField(height_field=b'height', width_field=b'width', upload_to=b'banner')),
            ],
            options={
                'verbose_name': 'Banner',
                'verbose_name_plural': 'Banners',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BannerType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=10, verbose_name='Code')),
                ('width', models.PositiveIntegerField(verbose_name='Expected banner width')),
                ('height', models.PositiveIntegerField(verbose_name='Expected banner height')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('description', models.CharField(max_length=100, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Banner type',
                'verbose_name_plural': 'Banner types',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='bannertype',
            unique_together=set([('code',)]),
        ),
        migrations.AddField(
            model_name='banner',
            name='banner_type',
            field=models.ForeignKey(to='advertisement.BannerType'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='banner',
            unique_together=set([('code',)]),
        ),
    ]
