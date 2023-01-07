from content.models import SiteSettings


class ContentRepository:

    def get_site_settings(self):
        return SiteSettings.objects.first()

content_repo = ContentRepository()