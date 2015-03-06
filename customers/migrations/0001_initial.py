# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import common.validators.regex
import django.utils.timezone
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('name', models.CharField(max_length=61, validators=[common.validators.regex.NameRegexValidator()])),
                ('phone_number', models.CharField(max_length=9, validators=[django.core.validators.RegexValidator('^09\\d{8}|0[2-8]\\d{7}$')])),
                ('email', models.EmailField(max_length=75)),
                ('city', models.CharField(max_length=40, validators=[common.validators.regex.NameRegexValidator(1)])),
                ('address', models.CharField(max_length=55, validators=[common.validators.regex.NameRegexValidator(3)])),
                ('content', models.TextField(max_length=1024)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
            },
            bases=(models.Model,),
        ),
    ]
