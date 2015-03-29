# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0005_auto_20150326_2331'),
    ]

    operations = [
        migrations.CreateModel(
            name='RandomTextSet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('code', models.SlugField(max_length=10, verbose_name='Code')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('description', models.CharField(max_length=100, verbose_name='Description')),
                ('text_set_type', models.ForeignKey(verbose_name='Text set type', to='advertisement.TextSetType')),
            ],
            options={
                'verbose_name': 'Random text set',
                'verbose_name_plural': 'Random text set',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RandomTextSetChoice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('weight', models.PositiveIntegerField(verbose_name='Weight', validators=[django.core.validators.MinValueValidator(1)])),
                ('remaining_hits', models.PositiveIntegerField(null=True, verbose_name='Remaining hits')),
                ('owner', models.ForeignKey(related_name='choices', verbose_name='Random owner', to='advertisement.RandomTextSet')),
                ('text_set', models.ForeignKey(verbose_name='Text set', to='advertisement.TextSet')),
            ],
            options={
                'verbose_name': 'Random text set choice',
                'verbose_name_plural': 'Random text set choices',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='randomtextsetchoice',
            unique_together=set([('owner', 'text_set')]),
        ),
        migrations.AlterUniqueTogether(
            name='randomtextset',
            unique_together=set([('code',)]),
        ),
        migrations.AlterModelOptions(
            name='randombannerchoice',
            options={'verbose_name': 'Random banner choice', 'verbose_name_plural': 'Random banner choices'},
        ),
    ]
