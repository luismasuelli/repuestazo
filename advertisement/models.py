from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import Max
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _


class BannerType(models.Model):
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


class Banner(models.Model):
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


class ReelType(models.Model):
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
    Permite listar reels que se encuentran listos (es decir: se excluyen los que no tienen imagenes cargadas).
    """

    def ready(self):
        return self.annotate(number_of_images=models.Count('image_list')).exclude(number_of_images=0)


class Reel(models.Model):
    """
    Define un reel, ligado a un tipo de reel.
    """

    reel_type = models.ForeignKey(ReelType, null=False, verbose_name=_(u'Reel type'))
    code = models.CharField(verbose_name=_(u'Code'), max_length=10, null=False)
    name = models.CharField(verbose_name=_(u'Name'), max_length=30, null=False)
    description = models.CharField(verbose_name=_(u'Description'), max_length=100, null=False)

    #manager personalizado
    objects = ReelQuerySet.as_manager()

    def ready(self):
        """
        Determina si puede ser mostrado (es decir: si tiene imagenes).
        """

        return self.image_list.exists()

    class Meta:
        unique_together = (('code',),)
        verbose_name = _(u'Reel')
        verbose_name_plural = _(u'Reels')


class ReelImage(models.Model):
    """
    Define una imagen de un reel, validando sus dimensiones.
    """

    reel = models.ForeignKey(Reel, null=False, verbose_name=_(u'Reel'), related_name='image_list')
    sequence = models.PositiveIntegerField(verbose_name=_(u'Sequence'), null=False, validators=[MinValueValidator(1)])
    name = models.CharField(verbose_name=_(u'Name'), max_length=30, null=False)
    description = models.CharField(verbose_name=_(u'Description'), max_length=100, null=False)

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