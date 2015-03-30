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
        migrations.CreateModel(
            name='Reel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reel_type', models.ForeignKey(verbose_name='Reel type', to='advertisement.ReelType')),
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
                ('height', models.PositiveIntegerField(verbose_name='Reel image height', editable=False)),
                ('width', models.PositiveIntegerField(verbose_name='Reel image width', editable=False)),
                ('image', models.ImageField(default=None, height_field=b'height', width_field=b'width', upload_to=b'reel')),
            ],
            options={
                'verbose_name': 'Reel image',
                'verbose_name_plural': 'Reel images',
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
        migrations.AlterModelOptions(
            name='reelimage',
            options={'ordering': ('reel', 'sequence'), 'verbose_name': 'Reel image', 'verbose_name_plural': 'Reel images'},
        ),
        migrations.AddField(
            model_name='banner',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='banner',
            name='updated_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bannertype',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bannertype',
            name='updated_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='reel',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='reel',
            name='updated_on',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='reelimage',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='reelimage',
            name='updated_on',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='reeltype',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='reeltype',
            name='updated_on',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reelimage',
            name='sequence',
            field=models.PositiveIntegerField(verbose_name='Sequence', validators=[django.core.validators.MinValueValidator(1)]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='banner',
            name='target',
            field=models.URLField(help_text='If set, the banner becomes a link', null=True, verbose_name='Target', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='reel',
            name='link_default',
            field=models.URLField(help_text='Default target URL for reel images', null=True, verbose_name='Default target', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='reel',
            name='link_prevails',
            field=models.BooleanField(default=False, help_text="Tells whether clicking any reel image will always make use of the default target instead of following the image's critera. Such criterion is only effective when the default target is set", verbose_name='Prevailing target'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='reelimage',
            name='link_own',
            field=models.URLField(help_text='A reel image will become a link if it has a value in this field, or the owner reel has something in the default target field. If neither of those cases occur, the reel image will not be a link', null=True, verbose_name='Target', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reelimage',
            name='image',
            field=models.ImageField(height_field=b'height', width_field=b'width', upload_to=b'reel'),
            preserve_default=True,
        ),
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
        migrations.AddField(
            model_name='textset',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='textset',
            name='updated_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='textsetelement',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='textsetelement',
            name='updated_on',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='textsettype',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='textsettype',
            name='updated_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='textsettypefield',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='textsettypefield',
            name='updated_on',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
            preserve_default=True,
        ),
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
            name='code',
            field=models.SlugField(max_length=10, verbose_name='Code'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reeltype',
            name='code',
            field=models.SlugField(max_length=10, verbose_name='Code'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='textset',
            name='code',
            field=models.SlugField(max_length=10, verbose_name='Code'),
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
            name='code',
            field=models.SlugField(max_length=10, verbose_name='Code'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='textsettype',
            name='code',
            field=models.SlugField(max_length=10, verbose_name='Code'),
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
            name='code',
            field=models.SlugField(max_length=10, verbose_name='Code'),
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
        migrations.AlterField(
            model_name='randombannerchoice',
            name='remaining_hits',
            field=models.PositiveIntegerField(null=True, verbose_name='Remaining hits', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='randomtextsetchoice',
            name='remaining_hits',
            field=models.PositiveIntegerField(null=True, verbose_name='Remaining hits', blank=True),
            preserve_default=True,
        ),
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
