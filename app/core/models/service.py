from django.db import models
from django.db.models.deletion import CASCADE 
from django.utils.translation import ugettext_lazy as _

from .base import BaseModel
from profiles.models import Business


class Service(BaseModel):
    business = models.ForeignKey(Business, on_delete=models.CASCADE, null=True, blank=True)

    name = models.CharField(max_length=200, verbose_name=_('Service name'), null=True, blank=True)
    description = models.TextField(verbose_name=_('Description'), null=True, blank=True)
    price = models.PositiveIntegerField(verbose_name=_('Price'), default=0, null=True, blank=True)
    url = models.URLField(verbose_name=_('URL'), null=True, blank=True)

    
    class Meta:
        verbose_name = _('Service')
        verbose_name_plural = _('Services')
    
    def __str__(self):
        return self.name