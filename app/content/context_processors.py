from content.repository import content_repo


def site_settings(request):
    return {
        'site_settings': content_repo.get_site_settings()
    }