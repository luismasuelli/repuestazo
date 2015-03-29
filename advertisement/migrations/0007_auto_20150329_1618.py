# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0006_auto_20150328_1951'),
    ]

    operations = [
        migrations.AddField(
            model_name='textsetelement',
            name='field',
            field=models.ForeignKey(default=None, verbose_name='Field', to='advertisement.TextSetTypeField'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='banner',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='banner',
            name='updated_on',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bannertype',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bannertype',
            name='updated_on',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='randombanner',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='randombanner',
            name='updated_on',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='randombannerchoice',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='randombannerchoice',
            name='updated_on',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='randomtextset',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='randomtextset',
            name='updated_on',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='randomtextsetchoice',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='randomtextsetchoice',
            name='updated_on',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reel',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reel',
            name='updated_on',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reelimage',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reelimage',
            name='updated_on',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reeltype',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reeltype',
            name='updated_on',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='textset',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='textset',
            name='updated_on',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='textsetelement',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='textsetelement',
            name='updated_on',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='textsettype',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='textsettype',
            name='updated_on',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='textsettypefield',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='textsettypefield',
            name='updated_on',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='textsetelement',
            unique_together=set([('field', 'owner')]),
        ),
        migrations.RemoveField(
            model_name='textsetelement',
            name='code',
        ),
    ]
