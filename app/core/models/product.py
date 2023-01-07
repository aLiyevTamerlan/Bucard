from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify

from core.models.base import BaseModel
from .image import Image


class Product(BaseModel):
    name = models.CharField(max_length=400, verbose_name=_('Name'))
    description = models.TextField(verbose_name=_('Description'), null=True, blank=True)
    price = models.DecimalField(verbose_name=_('Price'), max_digits=30, decimal_places=2, default=0)
    images = models.ManyToManyField(Image, verbose_name=_('Product images'), related_name='products', blank=True)

    business = models.ForeignKey('profiles.Business', on_delete=models.CASCADE, verbose_name=_('Business'), null=True, blank=True)
    slug = models.SlugField(verbose_name=_('Product slug'), unique=True, null=True, blank=True)


    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.name)
        super().save(*args, **kwargs)


