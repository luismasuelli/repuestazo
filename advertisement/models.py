from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import ugettext_lazy as _


class BannerType(models.Model):
    """
    Define un tipo de banner con su descripcion y dimensiones.
    """

    code = models.CharField(verbose_name=_(u'Code'),  max_length=10)
    width = models.PositiveIntegerField(verbose_name=_(u'Expected banner width'), null=False)
    height = models.PositiveIntegerField(verbose_name=_(u'Expected banner height'), null=False)
    name = models.CharField(verbose_name=_(u'Name'), max_length=30, null=False)
    description = models.CharField(verbose_name=_(u'Description'), max_length=100, null=False)

    class Meta:
        unique_together = (('code',),)
        verbose_name = _(u'Banner type')
        verbose_name_plural = _(u'Banner types')


class Banner(models.Model):
    """
    Define un banner, ligado al tipo de banner, validando dimensiones.
    """

    banner_type = models.ForeignKey(BannerType)
    code = models.SlugField(verbose_name=_(u'Code'), max_length=10, null=False)
    name = models.CharField(verbose_name=_(u'Name'), max_length=30, null=False)
    description = models.CharField(verbose_name=_(u'Description'), max_length=100, null=False)
    width = models.PositiveIntegerField(verbose_name=_(u'Banner width'), null=False, editable=False)
    height = models.PositiveIntegerField(verbose_name=_(u'Banner height'), null=False, editable=False)
    image = models.ImageField(upload_to='banner', null=False, height_field='height', width_field='width')

    def clean(self):
        try:
            if self.width != self.banner_type.width:
                raise ValidationError(_(u'Image width (currently: %(current)d) must be the expected in the banner '
                                        u'type (currently: %(expected)d)') % {'current': self.width, 'expected': self.banner_type.width})
            if self.height != self.banner_type.height:
                raise ValidationError(_(u'Image height (currently: %(current)d) must be the expected in the banner '
                                        u'type (currently: %(expected)d)') % {'current': self.height, 'expected': self.banner_type.height})
        except BannerType.DoesNotExist:
            pass

    class Meta:
        unique_together = (('code',),)
        verbose_name = _(u'Banner')
        verbose_name_plural = _(u'Banners')