from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.timezone import now


class Trackable(models.Model):
    """
    This model object can be trackable (create/edit dates are stored).
    """

    created_on = models.DateTimeField(default=now, null=False)
    updated_on = models.DateTimeField(default=now, null=False)

    class Meta:
        abstract = True


@receiver(pre_save, sender=Trackable)
def _save(sender, **kwargs):
    kwargs['instance'].updated_on = now()