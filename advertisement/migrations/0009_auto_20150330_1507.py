# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0008_auto_20150330_1059'),
    ]

    operations = [
        migrations.RenameField(
            model_name='textsetelement',
            old_name='field',
            new_name='text_field',
        ),
        migrations.AlterUniqueTogether(
            name='textsetelement',
            unique_together=set([('text_field', 'owner')]),
        ),
    ]
