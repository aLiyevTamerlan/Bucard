from django.db import models 
from django.utils.translation import ugettext_lazy as _

from .base import BaseModel


class PromoCode(BaseModel):
    name = models.CharField(max_length=80, verbose_name=_('Code'), help_text=_('Example: buca2020'), unique=True, null=True, blank=True)
    discount_percentage = models.PositiveIntegerField(verbose_name=_('Discount of promo code'), default=0)
    start_date = models.DateTimeField(verbose_name=_('Start date'), null=True, blank=True)
    expiration_date = models.DateTimeField(verbose_name=_('Expiration date'), help_text=_('Can be left blank'), null=True, blank=True)
    limit = models.PositiveIntegerField(verbose_name=_('Code limit'), default=0, help_text=_('Can be left blank'))
    is_active = models.BooleanField(verbose_name=_('Is active'), help_text=_('Will automatically be changed'), default=True)

    class Meta:
        verbose_name = _('Promo code')
        verbose_name_plural = _('Promo codes')

    def __str__(self) -> str:
        return self.name

