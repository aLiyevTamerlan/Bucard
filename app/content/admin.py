from django.contrib import admin

from content.models import SiteSettings


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = (
        'site_name',
        'site_description',
        'site_email',
        'contact_number',
        'contact_email',
        'fb_link',
        'twitter_link',
        'linkedin_link',
        'instagram_link',
    )