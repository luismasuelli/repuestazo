from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _
from common.apps.track.models import Trackable


class BannerType(Trackable):
    """
    Define un tipo de banner con su descripcion y dimensiones.
    """

    code = models.CharField(verbose_name=_(u'Code'),  max_length=10, null=False)
    width = models.PositiveIntegerField(verbose_name=_(u'Expected banner width'), null=False)
    height = models.PositiveIntegerField(verbose_name=_(u'Expected banner height'), null=False)
    name = models.CharField(verbose_name=_(u'Name'), max_length=30, null=False)
    description = models.CharField(verbose_name=_(u'Description'), max_length=100, null=False)

    class Meta:
        unique_together = (('code',),)
        verbose_name = _(u'Banner type')
        verbose_name_plural = _(u'Banner types')


class Banner(Trackable):
    """
    Define un banner, ligado al tipo de banner, validando dimensiones.
    """

    banner_type = models.ForeignKey(BannerType, null=False, verbose_name=_(u'Banner type'))
    code = models.SlugField(verbose_name=_(u'Code'), max_length=10, null=False)
    name = models.CharField(verbose_name=_(u'Name'), max_length=30, null=False)
    description = models.CharField(verbose_name=_(u'Description'), max_length=100, null=False)
    width = models.PositiveIntegerField(verbose_name=_(u'Banner width'), null=False, editable=False)
    height = models.PositiveIntegerField(verbose_name=_(u'Banner height'), null=False, editable=False)
    image = models.ImageField(upload_to='banner', null=False, height_field='height', width_field='width')
    target = models.URLField(verbose_name=_(u'Target'), help_text=_(u'If set, the banner becomes a link'),
                             null=True, blank=True)

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


class ReelType(Trackable):
    """
    Define un tipo de reel con su descripcion y dimensiones.
    """

    code = models.CharField(verbose_name=_(u'Code'), max_length=10, null=False)
    width = models.PositiveIntegerField(verbose_name=_(u'Expected reel width'), null=False,
                                        help_text=_(u'Each image in each reel with this type must have this width'))
    height = models.PositiveIntegerField(verbose_name=_(u'Expected reel height'), null=False,
                                         help_text=_(u'Each image in each reel with this type must have this height'))
    name = models.CharField(verbose_name=_(u'Name'), max_length=30, null=False)
    description = models.CharField(verbose_name=_(u'Description'), max_length=100, null=False)

    class Meta:
        unique_together = (('code',),)
        verbose_name = _(u'Reel type')
        verbose_name_plural = _(u'Reel types')


class ReelQuerySet(models.QuerySet):
    """
    Permite listar marquesinas que se encuentran listas (es decir: se excluyen las que no tienen imagenes cargadas).
    """

    def ready(self):
        """
        Excluimos las marquesinas que no tienen al menos una imagen cargada.
        """

        return self.annotate(number_of_images=models.Count('image_list')).exclude(number_of_images=0)


class Reel(Trackable):
    """
    Define un reel, ligado a un tipo de reel.
    """

    reel_type = models.ForeignKey(ReelType, null=False, verbose_name=_(u'Reel type'))
    code = models.CharField(verbose_name=_(u'Code'), max_length=10, null=False)
    name = models.CharField(verbose_name=_(u'Name'), max_length=30, null=False)
    description = models.CharField(verbose_name=_(u'Description'), max_length=100, null=False)
    link_default = models.URLField(verbose_name=_(u'Default target'), help_text=_(u'Default target URL for reel images'),
                                   null=True, blank=True)
    link_prevails = models.BooleanField(default=False, verbose_name=_(u'Prevailing target'), null=False,
                                        help_text=_(u'Tells whether clicking any reel image will always make use '
                                                    u'of the default target instead of following the image\'s critera. '
                                                    u'Such criterion is only effective when the default target is set'))

    #manager personalizado
    objects = ReelQuerySet.as_manager()

    def make_link(self, url):
        """
        Creates a link given the children image's link. It considers those by "or" operation, but
          with different "prevail" order for the calculation.
        """
        return self.link_default or url if self.link_prevails else url or self.link_default

    def ready(self):
        """
        Determina si puede ser mostrado (es decir: si tiene imagenes).
        """

        return self.image_list.exists()

    class Meta:
        unique_together = (('code',),)
        verbose_name = _(u'Reel')
        verbose_name_plural = _(u'Reels')


class ReelImage(Trackable):
    """
    Define una imagen de un reel, validando sus dimensiones.
    """

    reel = models.ForeignKey(Reel, null=False, verbose_name=_(u'Reel'), related_name='image_list')
    sequence = models.PositiveIntegerField(verbose_name=_(u'Sequence'), null=False, validators=[MinValueValidator(1)])
    name = models.CharField(verbose_name=_(u'Name'), max_length=30, null=False)
    description = models.CharField(verbose_name=_(u'Description'), max_length=100, null=False)
    width = models.PositiveIntegerField(verbose_name=_(u'Reel image width'), null=False, editable=False)
    height = models.PositiveIntegerField(verbose_name=_(u'Reel image height'), null=False, editable=False)
    image = models.ImageField(upload_to='reel', null=False, height_field='height', width_field='width')
    link_own = models.URLField(verbose_name=_(u'Target'), null=True, blank=True,
                               help_text=_(u'A reel image will become a link if it has a value in this field, or the '
                                           u'owner reel has something in the default target field. If neither of those '
                                           u'cases occur, the reel image will not be a link'))

    @property
    def target(self):
        """
        Obtiene la URL para la cual se transformara en un enlace.
        """

        try:
            return self.reel.make_link(self.link_own)
        except Reel.DoesNotExist:
            return None

    def clean(self):
        """
        Controla que las dimensiones encajen como debe ser, contra el tipo.
        """

        try:
            if self.width != self.reel.reel_type.width:
                raise ValidationError(_(u'Reel image width (currently: %(current)d) must be the expected in the reel '
                                        u'type (currently: %(expected)d)') % {'current': self.width, 'expected': self.reel.reel_type.width})
            if self.height != self.reel.reel_type.height:
                raise ValidationError(_(u'Reel image height (currently: %(current)d) must be the expected in the reel '
                                        u'type (currently: %(expected)d)') % {'current': self.height, 'expected': self.reel.reel_type.height})
        except Reel.DoesNotExist:
            pass

    class Meta:
        ordering = ('reel', 'sequence')
        unique_together = (('reel', 'sequence'),)
        verbose_name = _(u'Reel image')
        verbose_name_plural = _(u'Reel images')


@receiver(pre_save, sender=ReelImage)
def before_save_reel_image(sender, **kwargs):
    """
    Asigna un numero de secuencia automaticamente si es que no lo tiene.
    """
    instance = kwargs['instance']
    if not instance.sequence:
        sequence = 1
        for obj in instance.reel.all():
            if obj.sequence != sequence:
                break
            sequence += 1
        instance.sequence = sequence


class TextSetType(Trackable):
    """
    Define un preset de textos publicitarios (lineales, chicos).
    """

    code = models.CharField(verbose_name=_(u'Code'), max_length=10, null=False)
    name = models.CharField(verbose_name=_(u'Name'), max_length=30, null=False)
    description = models.CharField(verbose_name=_(u'Description'), max_length=100, null=False)

    class Meta:
        unique_together = (('code',),)
        verbose_name = _(u'Text set type')
        verbose_name_plural = _(u'Text set types')


class TextSetTypeField(Trackable):
    """
    Define una columna esperada para cierto preset. Se puede definir si la entrada es obligatoria o no.
    """

    owner = models.ForeignKey(TextSetType, null=False, verbose_name=_(u'Text set type'), related_name='fields')
    code = models.CharField(verbose_name=_(u'Code'), max_length=10, null=False)
    required = models.BooleanField(default=True, verbose_name=_(u'Required'), null=False)

    class Meta:
        unique_together = (('code', 'owner'),)
        verbose_name = _(u'Text set type field')
        verbose_name_plural = _(u'Text set type fields')


class TextSet(Trackable):
    """
    Define un conjunto de textos, para cierto tipo de texto.
    """

    text_set_type = models.ForeignKey(TextSetType, null=False, verbose_name=_(u'Text set type'), related_name='entries')
    code = models.CharField(verbose_name=_(u'Code'), max_length=10, null=False)

    class Meta:
        unique_together = (('code',),)
        verbose_name = _(u'Text set')
        verbose_name_plural = _(u'Text sets')


class TextSetElement(Trackable):
    """
    Define un texto, perteneciente a cierto conjunto de textos.
    """

    owner = models.ForeignKey(TextSet, null=False, verbose_name=_(u'Text set'), related_name='entries')
    code = models.CharField(verbose_name=_(u'Code'), max_length=10, null=False)
    value = models.CharField(max_length=255, null=False, blank=True, verbose_name=_(u'Content'))

    def clean(self):
        """
        Exige que el campo se requiera, si corresponde, y exista en el tipo.
        """

        try:
            field = self.owner.text_set_type.fields.get(code=self.code)
            if not self.value and field.required:
                raise ValidationError(_(u'The value must not be empty since the owner entry\'s type defines this field as required'))
        except TextSet.DoesNotExist:
            pass
        except TextSetTypeField.DoesNotExist:
            raise ValidationError(_(u'Text set element has an unexpected code (%(code)s) regarding its owner set') % {'code': self.code})

    class Meta:
        unique_together = (('code', 'owner'),)
        verbose_name = _(u'Text set element')
        verbose_name_plural = _(u'Text set elements')