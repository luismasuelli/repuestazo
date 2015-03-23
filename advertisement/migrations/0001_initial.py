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
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='reel',
            name='updated_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='reelimage',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='reelimage',
            name='updated_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='reeltype',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='reeltype',
            name='updated_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reelimage',
            name='sequence',
            field=models.PositiveIntegerField(verbose_name='Sequence', validators=[django.core.validators.MinValueValidator(1)]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='reelimage',
            name='height',
            field=models.PositiveIntegerField(default=0, verbose_name='Reel image height', editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reelimage',
            name='image',
            field=models.ImageField(default=None, height_field=b'height', width_field=b'width', upload_to=b'reel'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reelimage',
            name='width',
            field=models.PositiveIntegerField(default=0, verbose_name='Reel image width', editable=False),
            preserve_default=False,
        ),
    ]
