from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
from django.urls import reverse
# from django.contrib.sites.models import Site

from users.models import User
from app.utils.base_model import BaseModel


# domain = Site.objects.get_current().domain


class Business(BaseModel):
    BUSINESS_TYPES = (
        (1, 'Business'),
        (2, 'Company'),
    )
    name = models.CharField(max_length=200, verbose_name=_('Name'), unique=True)
    description = models.TextField(verbose_name=_('Overall description'), null=True, blank=True)
    manager = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        verbose_name=_('Manager'),
        null=True,
        blank=True
    )
    about = models.TextField(verbose_name='About business', null=True, blank=True)
    type = models.IntegerField(choices=BUSINESS_TYPES, default=1, verbose_name=_('Business type'))
    slug = models.SlugField(verbose_name=_('Slug'), unique=True, null=True, blank=True)
    qr_code = models.ImageField(verbose_name=_('QR Code'), null=True, blank=True, upload_to='qrs')

   
    ### Saved profiles ###
    saved_business = models.ManyToManyField('profiles.Business', verbose_name=_('Saved businesses'), related_name=_('businesses'), symmetrical=False, blank=True)
    saved_standard_profile = models.ManyToManyField('profiles.StandardProfile', verbose_name=_('Saved standard profiles'), related_name=_('businesses'), symmetrical=False, blank=True)
    saved_pro_profile = models.ManyToManyField('profiles.ProProfile', verbose_name=_('Saved pro profiles'), related_name=_('businesses'), symmetrical=False, blank=True)
    
    ### Contacts ###
    mobile_number = models.CharField(max_length=200, verbose_name=_('Mobile number'), null=True, blank=True)
    fax_number = models.CharField(max_length=200, verbose_name=_('FAX number'), null=True, blank=True)
    email_address = models.EmailField(verbose_name=_('E-Mail address'), null=True, blank=True)

    ### Social Media ###
    fb = models.URLField(verbose_name=_('Facebook profile/page url'), null=True, blank=True)
    linkedin = models.URLField(verbose_name=_('LinkedIn profile url'), null=True, blank=True)
    ig = models.URLField(verbose_name=_('Instagram profile url'), null=True, blank=True)
    vk = models.URLField(verbose_name=_('Vkontakte profile url'), null=True, blank=True)


    class Meta:
        verbose_name = _('Business')
        verbose_name_plural = _('Businesses')
    
    def __str__(self):
        return self.name   
    
    # def get_full_path(self):
    #     url = 'https://{domain}/business/{path}'.format(domain=domain, path=self.slug)

    #     return url
    
    def get_saved_profiels_count(self):
        results = {
            'vip_profile': self.saved_vip_profiles.all().count(),
            'standard_profiles': self.saved_standard_profiles.all().count(),
            'businesses': self.saved_businesses.all().count(),
        }

        return results

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.name)
        super().save(*args, **kwargs)