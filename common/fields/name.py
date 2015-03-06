from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator
from django.db.models import CharField
import unicodedata
import six
import re


_RX_LATIN = RegexValidator(r'^\s*[A-Za-z]+(\'[A-Za-z]+)?(\s+[A-Za-z]+(\'[A-Za-z]+)?)*\s*$',
                           message=_(u'Enter a valid name value'), code='invalid_name', flags=re.IGNORECASE)

_RX_LATIN_NUMS = RegexValidator(r'^\s*([A-Za-z]+(\'[A-Za-z]+)?|\d+)(\s+([A-Za-z]+(\'[A-Za-z]+)?|\d+))*\s*$',
                                message=_(u'Enter a valid name value'), code='invalid_name', flags=re.IGNORECASE)


def _normalize(value):
    return ''.join(c for c in unicodedata.normalize('NFD', six.text_type(value)) if unicodedata.category(c) != 'Mn')


name_field_error_messages = CharField.default_error_messages.copy()
name_field_error_messages['invalid_name'] = _('Enter a valid name value')


class NameField(CharField):

    default_error_messages = name_field_error_messages

    def __init__(self, allow_numbers=False, *args, **kwargs):
        super(NameField, self).__init__(*args, **kwargs)
        if allow_numbers:
            validator = lambda v: _RX_LATIN_NUMS(_normalize(v))
        else:
            validator = lambda v: _RX_LATIN(_normalize(v))
        self.validators.append()
