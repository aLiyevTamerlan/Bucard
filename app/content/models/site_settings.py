from django.db import models
from django.core.exceptions import ValidationError

from app.utils.base_model import BaseModel


class SiteSettings(BaseModel):
    site_name = models.CharField(max_length=255, default='Bucard')
    site_description = models.TextField(default='Site Description')
    site_logo = models.ImageField(
        upload_to='site_settings/', 
        blank=True, null=True
    )
    site_favicon = models.ImageField(
        upload_to='site_settings/', 
        blank=True, null=True
    )
    site_email = models.EmailField(
        verbose_name='Site Email',
        max_length=255,
        null=True, blank=True,
    )
    contact_number = models.CharField(
        verbose_name='Contact Number',
        max_length=255,
        null=True, blank=True,
    )
    contact_email = models.EmailField(
        verbose_name='Contact Email',
        max_length=255,
        null=True, blank=True,
    )
    fb_link = models.URLField(
        verbose_name='Facebook Link',
        max_length=255,
        null=True, blank=True,
    )
    twitter_link = models.URLField(
        verbose_name='Twitter Link',
        max_length=255,
        null=True, blank=True,
    )
    linkedin_link = models.URLField(
        verbose_name='Linkedin Link',
        max_length=255,
        null=True, blank=True,
    )
    instagram_link = models.URLField(
        verbose_name='Instagram Link',
        max_length=255,
        null=True, blank=True,
    )

    class Meta:
        verbose_name = 'Site Setting'
        verbose_name_plural = 'Site Settings'

    def save(self, *args, **kwargs):
        if not self.pk and SiteSettings.objects.exists():
            raise ValidationError('There is can be only one Site Settings instance')
        return super(SiteSettings, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.site_name