# coding=utf-8
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
import unicodedata
import re


class Country(models.Model):
    """
    País emisor de documento.
    """

    code = models.CharField(max_length=2, null=False, unique=True)
    name = models.CharField(max_length=100, null=False)

    class Meta:
        ordering = ("name",)
        verbose_name = _(u"Country")
        verbose_name_plural = _(u"Countries")

    def __unicode__(self):
        return "(%s) %s" % (self.code, self.name)


class LatinNamed(models.Model):

    RX_LATIN = RegexValidator(r'^\s*[A-Za-z]+(\'[A-Za-z]+)?(\s+[A-Za-z]+(\'[A-Za-z]+)?)*\s*$', _(u''), flags=re.IGNORECASE)

    @staticmethod
    def _normalize(value):
        return ''.join(c for c in unicodedata.normalize('NFD', value) if unicodedata.category(c) != 'Mn')

    @staticmethod
    def clean_latin(value):
        LatinNamed.RX_LATIN(LatinNamed._normalize(value))

    first_name = models.CharField(max_length=30, null=False, blank=False, validators=[lambda v: LatinNamed.clean_latin(v)])
    last_name = models.CharField(max_length=30, null=False, blank=False, validators=[lambda v: LatinNamed.clean_latin(v)])


class EcuadoreanCustomerIdentification(models.Model):
    """
    Trait de datos basicos de la consulta. Valida datos de identificacion.
    """

    ID_TYPE_NATIONAL = 1
    ID_TYPE_FOREIGN = 2
    ID_TYPES = (
        (ID_TYPE_NATIONAL, _(u'Cédula')),
        (ID_TYPE_FOREIGN, _(u'Pasaporte'))
    )

    identification = models.CharField(max_length=10, null=False, blank=False)
    identification_type = models.PositiveSmallIntegerField(null=False, choices=ID_TYPES)
    identification_country = models.ForeignKey(Country, to_field='code', null=False, related_name='%(class)_set')

    def _clean_national_identification(self):
        """
        Cross-validates national identification data (Ecuador).
        :return:
        """
        if self.identification_country_id != 'EC':
            raise ValidationError(_(u'Must use Ecuador as country for citizen IDs'))

    def _clean_foreign_identification(self):
        """
        Cross-validates foreign identification data (Ecuador).
        :return:
        """
        if self.identification_country_id == 'EC':
            raise ValidationError(_(u'Cannot use Ecuador as country for passports'))

    def clean(self):
        """
        Cross-validates identification data (Ecuador)
        :return:
        """

        if self.identification_type == self.ID_TYPE_NATIONAL:
            self._clean_national_identification()
        elif self.identification_type == self.ID_TYPE_FOREIGN:
            self._clean_foreign_identification()

    class Meta:
        abstract = True