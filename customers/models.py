# coding=utf-8
from __future__ import unicode_literals
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
from common.validators.regex import NameRegexValidator
from common.apps.track.models import Trackable


class Contact(Trackable):
    """
    A quite basic contact request
    """

    name = models.CharField(max_length=61, null=False, validators=[NameRegexValidator()])
    phone_number = models.CharField(max_length=9, null=False, validators=[RegexValidator('^09\d{8}|0[2-8]\d{7}$')])
    email = models.EmailField(null=False)
    city = models.CharField(max_length=40, null=False, validators=[NameRegexValidator(NameRegexValidator.MODE_ACCEPT_NUMBERS)])
    address = models.CharField(max_length=55, null=False, validators=[NameRegexValidator(NameRegexValidator.MODE_ALPHANUMERIC_EXTENDED)])
    content = models.TextField(max_length=1024, null=False)

    class Meta:
        abstract = False
        verbose_name = _('Contact')
        verbose_name_plural = _('Contacts')