from django.db import models
from django.utils.translation import ugettext_lazy as _
from common.apps.track.models import Trackable
from tinymce.models import HTMLField
from django.utils.text import slugify


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

    def for_category(self, category):
        return self.filter(category=category)

    def for_year(self, year):
        return self.filter(created_on__year=year)

    def for_month(self, year, month):
        return self.filter(created_on__year=year,
                           created_on__month=month)


class Entry(Trackable):
    """
    Entrada de blog.
    """

    category = models.ForeignKey(Category)
    slug = models.CharField(max_length=50, null=False, blank=True, verbose_name=_(u'Slug'))
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name=_(u'Title'))
    content = HTMLField(max_length=16777215, null=False, blank=False, verbose_name=_(u'Content'))

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
        return super(Entry, self).save(*args, **kwargs)