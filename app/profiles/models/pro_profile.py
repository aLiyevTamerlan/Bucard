from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify

from app.utils.base_model import BaseModel
from users.models import User


class ProProfile(BaseModel):
    ### TO DO: ADD KEYWORDS, PROFILE IMAGE AND PORTFOLIO FIELDS ### 
    user = models.OneToOneField(User, verbose_name=_('User'), related_name='pro_profile', on_delete=models.CASCADE)
    about = models.TextField(verbose_name=_('About'), null=True, blank=True)
    phone_number = models.CharField(verbose_name=_('Phone number'), max_length=100, null=True, blank=True)
    slug = models.SlugField(verbose_name=_('Slug'), unique=True, null=True, blank=True)
    profile_image = models.ImageField(verbose_name=_('Profile image'), upload_to='profile/', null=True, blank=True)
    qr_code = models.ImageField(verbose_name=_('QR Code'), null=True, blank=True, upload_to='qrs')  
    private_account= models.BooleanField(default=False)
    profile_link = models.URLField(max_length = 200, null=True, blank=True)
    keywords = models.ManyToManyField('profiles.Keyword', related_name=_('pro_profiles'), symmetrical=False)
    
    ### Saved profiles ###
    saved_business = models.ManyToManyField('profiles.Business', verbose_name=_('Saved businesses'), related_name=_('pro_profiles'), symmetrical=False, blank=True)
    saved_standard_profile = models.ManyToManyField('profiles.StandardProfile', verbose_name=_('Saved standard profiles'), related_name=_('pro_profiles'), symmetrical=False, blank=True)
    saved_pro_profile = models.ManyToManyField('ProProfile', verbose_name=_('Saved pro profiles'), related_name=_('pro_profiles'), symmetrical=False, blank=True)
    
    class Meta:
        verbose_name = _('Pro Profile')
        verbose_name_plural = _('Pro Profiles')

    def __str__(self):
        return self.user.email    

    def get_full_name(self):
        return f'{self.user.name} {self.user.surname}'
    
    def get_saved_profiles_count(self):
        results = {
            'pro_profile': self.saved_pro_profile.all().count(),
            'standard_profiles': self.saved_standard_profile.all().count(),
            'businesses': self.saved_business.all().count(),
        }

        return results
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug=slugify(f'{self.user.name}-{self.user.pk}')
        super().save(*args, **kwargs)