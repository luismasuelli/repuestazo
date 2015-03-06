# coding=utf-8
from __future__ import unicode_literals
from django.db import models
from django.utils.six import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class Country(models.Model):
    """
    A country, given by name and country code
    """

    code = models.CharField(max_length=2, null=False, unique=True)
    name = models.CharField(max_length=100, null=False)

    class Meta:
        ordering = ("name",)
        verbose_name = _(u"Country")
        verbose_name_plural = _(u"Countries")

    def __str__(self):
        return "(%s) %s" % (self.code, self.name)