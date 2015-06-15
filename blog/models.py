# coding=utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _
from common.apps.track.models import Trackable
from tinymce.models import HTMLField
from django.utils.text import slugify
from django.utils.html import strip_tags
import html
import HTMLParser


escape = html.escape
unescape = HTMLParser.HTMLParser().unescape


class Category(models.Model):
    """
    Categoria de entradas de blog.
    """

    code = models.SlugField(max_length=20, null=False, blank=True, unique=True, verbose_name=_(u'Code'))
    name = models.CharField(max_length=40, null=False, blank=False, verbose_name=_(u'Name'))
    description = models.CharField(max_length=255, null=False, blank=False, verbose_name=_(u'Description'))

    def save(self, *args, **kwargs):
        strip = lambda s: s.strip() if isinstance(s, (str, unicode)) else s
        self.name = strip(self.name)
        self.code = slugify(strip(self.code) or self.name)
        self.description = strip(self.description)
        return super(Category, self).save(*args, **kwargs)

    def __unicode__(self):
        return u'%s - %s' % (self.code, self.name)

    class Meta:
        abstract = False
        verbose_name = _(u'Category')
        verbose_name_plural = _(u'Categories')


class EntryQueryset(models.QuerySet):
    """
    Metodos de queryset adicionales para el blog.
    """

    def preview(self):
        return self.defer(None).defer('content')

    def full(self):
        return self.defer(None).defer('preview')

    def for_category(self, category):
        return self.filter(category=category)

    def for_year(self, year):
        return self.filter(created_on__year=year)

    def for_month(self, year, month):
        return self.filter(created_on__year=year, created_on__month=month)


class Entry(Trackable):
    """
    Entrada de blog.
    """

    category = models.ForeignKey(Category)
    slug = models.CharField(max_length=50, null=False, blank=True, verbose_name=_(u'Slug'))
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name=_(u'Title'))
    content = HTMLField(max_length=16777215, null=False, blank=False, verbose_name=_(u'Content'))
    preview = models.TextField(null=False, blank=False, verbose_name=_(u'Preview'))

    objects = EntryQueryset.as_manager()

    def __unicode__(self):
        return u"%s en %s - %s" % (self.created_on.strftime('%d/%m/%Y %H:%M'), self.category, self.title)

    class Meta:
        abstract = False
        verbose_name = _(u'Entry')
        verbose_name_plural = _(u'Entries')

    def save(self, *args, **kwargs):
        strip = lambda s: s.strip() if isinstance(s, (str, unicode)) else s
        self.title = strip(self.title)
        self.slug = slugify(strip(self.slug) or self.title)
        self.content = strip(self.content)
        self.preview = escape(unescape(strip_tags(self.content))[0:512])
        return super(Entry, self).save(*args, **kwargs)


class MonthEntriesBreakdownQueryset(models.QuerySet):
    """
    Consulta para el respectivo corte de control..
    """

    def do(self):
        return self.raw("""
        select @id := @id + 1 as id, year(created_on) as created_year, month(created_on) as created_month, count(1) as entries_count
        from %s t, (SELECT @i:=0) c
        group by created_year, created_month
        order by created_year DESC, created_month DESC
        """ % Entry._meta.db_table)


class MonthEntriesBreakdown(models.Model):
    """
    Corte de control (agrupacion) de año/mes/#entradas.
    """

    created_year = models.PositiveSmallIntegerField(null=False)
    created_month = models.PositiveSmallIntegerField(null=False)
    entries_count = models.PositiveIntegerField(null=False)
    objects = MonthEntriesBreakdownQueryset.as_manager()

    class Meta:
        managed = False
