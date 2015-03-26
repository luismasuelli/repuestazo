# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0002_auto_20150322_2259'),
    ]

    operations = [
        migrations.CreateModel(
            name='TextSet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=10, verbose_name='Code')),
            ],
            options={
                'verbose_name': 'Text set',
                'verbose_name_plural': 'Text sets',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TextSetElement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=10, verbose_name='Code')),
                ('value', models.CharField(max_length=255, verbose_name='Content', blank=True)),
                ('owner', models.ForeignKey(related_name='entries', verbose_name='Text set', to='advertisement.TextSet')),
            ],
            options={
                'verbose_name': 'Text set element',
                'verbose_name_plural': 'Text set elements',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TextSetType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=10, verbose_name='Code')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('description', models.CharField(max_length=100, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Text set type',
                'verbose_name_plural': 'Text set types',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TextSetTypeField',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=10, verbose_name='Code')),
                ('required', models.BooleanField(default=True, verbose_name='Required')),
                ('owner', models.ForeignKey(related_name='fields', verbose_name='Text set type', to='advertisement.TextSetType')),
            ],
            options={
                'verbose_name': 'Text set type field',
                'verbose_name_plural': 'Text set type fields',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='textsettypefield',
            unique_together=set([('code', 'owner')]),
        ),
        migrations.AlterUniqueTogether(
            name='textsettype',
            unique_together=set([('code',)]),
        ),
        migrations.AlterUniqueTogether(
            name='textsetelement',
            unique_together=set([('code', 'owner')]),
        ),
        migrations.AddField(
            model_name='textset',
            name='text_set_type',
            field=models.ForeignKey(related_name='entries', verbose_name='Text set type', to='advertisement.TextSetType'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='textset',
            unique_together=set([('code',)]),
        ),
    ]
