from django.views.generic import TemplateView


class FreePageView(TemplateView):
    template_name = 'user-profiles/free_profile.html'