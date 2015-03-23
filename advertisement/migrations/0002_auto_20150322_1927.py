# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=10, verbose_name='Code')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('description', models.CharField(max_length=100, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Reel',
                'verbose_name_plural': 'Reels',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ReelImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sequence', models.PositiveIntegerField(verbose_name='Sequence')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('description', models.CharField(max_length=100, verbose_name='Description')),
                ('reel', models.ForeignKey(related_name='image_list', verbose_name='Reel', to='advertisement.Reel')),
            ],
            options={
                'verbose_name': 'Reel image',
                'verbose_name_plural': 'Reel images',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ReelType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=10, verbose_name='Code')),
                ('width', models.PositiveIntegerField(help_text='Each image in each reel with this type must have this width', verbose_name='Expected reel width')),
                ('height', models.PositiveIntegerField(help_text='Each image in each reel with this type must have this height', verbose_name='Expected reel height')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('description', models.CharField(max_length=100, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Reel type',
                'verbose_name_plural': 'Reel types',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='reeltype',
            unique_together=set([('code',)]),
        ),
        migrations.AlterUniqueTogether(
            name='reelimage',
            unique_together=set([('reel', 'sequence')]),
        ),
        migrations.AddField(
            model_name='reel',
            name='reel_type',
            field=models.ForeignKey(verbose_name='Reel type', to='advertisement.ReelType'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='reel',
            unique_together=set([('code',)]),
        ),
        migrations.AlterField(
            model_name='banner',
            name='banner_type',
            field=models.ForeignKey(verbose_name='Banner type', to='advertisement.BannerType'),
            preserve_default=True,
        ),
    ]
