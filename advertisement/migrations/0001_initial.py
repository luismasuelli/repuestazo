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
            name='Banner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_on', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('code', models.SlugField(max_length=10, verbose_name='Code')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('description', models.CharField(max_length=100, verbose_name='Description')),
                ('width', models.PositiveIntegerField(verbose_name='Banner width', editable=False)),
                ('height', models.PositiveIntegerField(verbose_name='Banner height', editable=False)),
                ('image', models.ImageField(height_field=b'height', width_field=b'width', upload_to=b'banner')),
                ('target', models.URLField(help_text='If set, the banner becomes a link', null=True, verbose_name='Target', blank=True)),
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
                ('created_on', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_on', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
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
        migrations.CreateModel(
            name='RandomBanner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_on', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
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
                ('created_on', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_on', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('weight', models.PositiveIntegerField(verbose_name='Weight', validators=[django.core.validators.MinValueValidator(1)])),
                ('remaining_hits', models.PositiveIntegerField(null=True, verbose_name='Remaining hits', blank=True)),
                ('banner', models.ForeignKey(verbose_name='Banner', to='advertisement.Banner')),
                ('owner', models.ForeignKey(related_name='choices', verbose_name='Random owner', to='advertisement.RandomBanner')),
            ],
            options={
                'verbose_name': 'Random banner choice',
                'verbose_name_plural': 'Random banner choices',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RandomTextSet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_on', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('code', models.SlugField(max_length=10, verbose_name='Code')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('description', models.CharField(max_length=100, verbose_name='Description')),
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
                ('created_on', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_on', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('weight', models.PositiveIntegerField(verbose_name='Weight', validators=[django.core.validators.MinValueValidator(1)])),
                ('remaining_hits', models.PositiveIntegerField(null=True, verbose_name='Remaining hits', blank=True)),
                ('owner', models.ForeignKey(related_name='choices', verbose_name='Random owner', to='advertisement.RandomTextSet')),
            ],
            options={
                'verbose_name': 'Random text set choice',
                'verbose_name_plural': 'Random text set choices',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Reel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_on', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('code', models.SlugField(max_length=10, verbose_name='Code')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('description', models.CharField(max_length=100, verbose_name='Description')),
                ('link_default', models.URLField(help_text='Default target URL for reel images', null=True, verbose_name='Default target', blank=True)),
                ('link_prevails', models.BooleanField(default=False, help_text="Tells whether clicking any reel image will always make use of the default target instead of following the image's critera. Such criterion is only effective when the default target is set", verbose_name='Prevailing target')),
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
                ('created_on', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_on', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('sequence', models.PositiveIntegerField(verbose_name='Sequence', validators=[django.core.validators.MinValueValidator(1)])),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('description', models.CharField(max_length=100, verbose_name='Description')),
                ('width', models.PositiveIntegerField(verbose_name='Reel image width', editable=False)),
                ('height', models.PositiveIntegerField(verbose_name='Reel image height', editable=False)),
                ('image', models.ImageField(height_field=b'height', width_field=b'width', upload_to=b'reel')),
                ('link_own', models.URLField(help_text='A reel image will become a link if it has a value in this field, or the owner reel has something in the default target field. If neither of those cases occur, the reel image will not be a link', null=True, verbose_name='Target', blank=True)),
                ('reel', models.ForeignKey(related_name='image_list', verbose_name='Reel', to='advertisement.Reel')),
            ],
            options={
                'ordering': ('reel', 'sequence'),
                'verbose_name': 'Reel image',
                'verbose_name_plural': 'Reel images',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ReelType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_on', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('code', models.SlugField(max_length=10, verbose_name='Code')),
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
        migrations.CreateModel(
            name='TextSet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_on', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('code', models.SlugField(max_length=10, verbose_name='Code')),
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
                ('created_on', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_on', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
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
                ('created_on', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_on', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('code', models.SlugField(max_length=10, verbose_name='Code')),
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
                ('created_on', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_on', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('code', models.SlugField(max_length=10, verbose_name='Code')),
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
        migrations.AddField(
            model_name='textsetelement',
            name='text_field',
            field=models.ForeignKey(verbose_name='Field', to='advertisement.TextSetTypeField'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='textsetelement',
            unique_together=set([('text_field', 'owner')]),
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
        migrations.AddField(
            model_name='randomtextsetchoice',
            name='text_set',
            field=models.ForeignKey(verbose_name='Text set', to='advertisement.TextSet'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='randomtextsetchoice',
            unique_together=set([('owner', 'text_set')]),
        ),
        migrations.AddField(
            model_name='randomtextset',
            name='text_set_type',
            field=models.ForeignKey(verbose_name='Text set type', to='advertisement.TextSetType'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='randomtextset',
            unique_together=set([('code',)]),
        ),
        migrations.AlterUniqueTogether(
            name='randombannerchoice',
            unique_together=set([('owner', 'banner')]),
        ),
        migrations.AlterUniqueTogether(
            name='randombanner',
            unique_together=set([('code',)]),
        ),
        migrations.AlterUniqueTogether(
            name='bannertype',
            unique_together=set([('code',)]),
        ),
        migrations.AddField(
            model_name='banner',
            name='banner_type',
            field=models.ForeignKey(verbose_name='Banner type', to='advertisement.BannerType'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='banner',
            unique_together=set([('code',)]),
        ),
    ]
