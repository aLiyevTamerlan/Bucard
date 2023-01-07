from django.views.generic import TemplateView


class ProPageView(TemplateView):
    template_name = 'user-profiles/pro_profile.html'