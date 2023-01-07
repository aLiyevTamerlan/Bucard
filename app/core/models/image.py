from django.db import models
from django.utils.translation import ugettext_lazy as _

from .base import BaseModel
from profiles.models import ProProfile


class Image(BaseModel):    
    image = models.ImageField(verbose_name=_('Image'))

    class Meta:
        verbose_name = _('Image')
        verbose_name_plural = _('Images')
    