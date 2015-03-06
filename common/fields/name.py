from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator
from django.db.models import CharField
import unicodedata
import six
import re


_RX_LATIN = RegexValidator(r'^\s*[A-Za-z]+(\'[A-Za-z]+)?(\s+[A-Za-z]+(\'[A-Za-z]+)?)*\s*$',
                           message=_(u'Enter a valid name value'), code='invalid_name', flags=re.IGNORECASE)


def _normalize(value):
    return ''.join(c for c in unicodedata.normalize('NFD', six.text_type(value)) if unicodedata.category(c) != 'Mn')


name_field_error_messages = CharField.default_error_messages.copy()
name_field_error_messages['invalid_name'] = _('Enter a valid name value')


class NameField(CharField):

    default_error_messages = name_field_error_messages

    def __init__(self, *args, **kwargs):
        super(NameField, self).__init__(*args, **kwargs)
        self.validators.append(lambda v: _RX_LATIN(_normalize(v)))
