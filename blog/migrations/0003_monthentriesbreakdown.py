# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150418_1934'),
    ]

    operations = [
        migrations.CreateModel(
            name='MonthEntriesBreakdown',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_year', models.PositiveSmallIntegerField()),
                ('created_month', models.PositiveSmallIntegerField()),
                ('entries_count', models.PositiveIntegerField()),
            ],
            options={
                'managed': False,
            },
        ),
    ]
