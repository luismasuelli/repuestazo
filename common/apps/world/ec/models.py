from __future__ import unicode_literals
from ...world.countries.models import Country
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import ugettext_lazy as _
import re


class EcuadoreanIdentification(models.Model):
    """
    Identificacion ecuatoriana - modelo abstracto
    """

    ID_TYPE_NATIONAL = 1
    ID_TYPE_FOREIGN = 2
    ID_TYPES = (
        (ID_TYPE_NATIONAL, _('Citizen ID')),
        (ID_TYPE_FOREIGN, _('Passport'))
    )

    identification = models.CharField(max_length=10, null=False, blank=False)
    identification_type = models.PositiveSmallIntegerField(null=False, choices=ID_TYPES)
    identification_country = models.ForeignKey(Country, to_field='code', null=False)

    def _clean_national_identification(self):
        """
        Cross-validates national identification data (Ecuador).
        :return:
        """
        if self.identification_country_id != 'EC':
            raise ValidationError(_(u'Must use Ecuador as country for citizen IDs'))

        if not re.match('^\d{10}$', self.identification):
            raise ValidationError(_(u'Ecuadorean identifier ID must be 10 digits long'))

        coeficientes = [2, 1, 2, 1, 2, 1, 2, 1, 2]
        digits = [int(v) for v in self.identification[:9]]
        reduce9 = lambda x: x - 9 if x > 9 else x
        reduced = [reduce9(a * b) for (a, b) in zip(coeficientes, digits)]
        weighted = sum(reduced)
        modulo = weighted % 10
        modulo = (10 - modulo) if modulo != 0 else 0
        province = int(self.identification[:2])
        verifier = int(self.identification[9])
        person_type = int(self.identification[2])

        if province not in xrange(1, 25):
            raise ValidationError(_(u'Invalid ecuadorean identifier'), 'invalid-content')

        if person_type not in xrange(0, 6):
            raise ValidationError(_(u'Invalid ecuadorean identifier'), 'invalid-content')

        if verifier != modulo:
            raise ValidationError(_(u'Invalid ecuadorean identifier'), 'invalid-content')

    def _clean_foreign_identification(self):
        """
        Cross-validates foreign identification data (Ecuador).
        :return:
        """
        if self.identification_country_id == 'EC':
            raise ValidationError(_(u'Cannot use Ecuador as country for passports'))

        if not re.match('^[A-Z0-9]{6,9}$', self.identification):
            raise ValidationError(_(u'Passport must be an alphanumeric string of 6-9 characters'))

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