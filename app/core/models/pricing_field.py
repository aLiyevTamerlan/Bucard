from django.db import models 
from django.utils.translation import ugettext_lazy as _

from app.utils.base_model import BaseModel


class PricingField(BaseModel):
    pricing = models.ForeignKey(
        'core.Pricing',
        verbose_name = _('Pricing'),
        related_name = 'fields',
        on_delete = models.CASCADE
    )
    title = models.CharField(
        verbose_name = _('Field name'),
        max_length = 200
    )

    class Meta:
        verbose_name = _('Field')
        verbose_name = _('Fields')
    
    def __str__(self):
        return self.title