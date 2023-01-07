from django.db import models
from django.utils.translation import ugettext_lazy as _

from app.utils import PROFILE_CHOICES
from app.utils.base_model import BaseModel


class Pricing(BaseModel):
    monthly_price = models.FloatField(
        verbose_name=_("Monthly Price"),
        default=0
    )
    yearly_price = models.FloatField(
        verbose_name=_("Yearly Price"),
        default=0
    )
    choice = models.CharField(
        verbose_name=_("Profile Choice"),
        choices=PROFILE_CHOICES,
        max_length=200,
        default="blank"
    )

    class Meta:
        verbose_name = _("Pricing")
        verbose_name_plural = _("Pricings")
    
    def __str__(self):
        return self.choice
