from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.timezone import now


class Trackable(models.Model):
    """
    This model object can be trackable (create/edit dates are stored).
    """

    created_on = models.DateTimeField(default=now, null=False, editable=False)
    updated_on = models.DateTimeField(default=now, null=False, editable=False)

    class Meta:
        abstract = True

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.updated_on = now()
        return super(Trackable, self).save(force_insert, force_update, using, update_fields)