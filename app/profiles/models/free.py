from django import utils
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify

from app.utils.base_model import BaseModel
from users.models import User


class FreeProfile(BaseModel):
    user = models.OneToOneField(User, verbose_name=_('User'), related_name='free_profile', on_delete=models.CASCADE)
    slug = models.SlugField(verbose_name=_('Slug'), unique=True, null=True, blank=True)

    ### Saved profiles ###
    business_profiles = models.ManyToManyField('profiles.Business', verbose_name=_('Saved business'), related_name=_('free_profiles'), symmetrical=False, blank=True)
    standard_profiles = models.ManyToManyField('profiles.StandardProfile', verbose_name=_('Saved standard profile'), related_name=_('free_profiles'), symmetrical=False, blank=True)
    pro_profiles = models.ManyToManyField('profiles.ProProfile', verbose_name=_('Saved pro profile'), related_name=_('free_profiles'), symmetrical=False, blank=True)

    class Meta:
        verbose_name = _('Free profile')
        verbose_name_plural = _('Free profiles')
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug=slugify(f'{self.user.pk}')
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.user.email