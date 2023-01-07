from django.views.generic import TemplateView


class StandartPageView(TemplateView):
    template_name = 'user-profiles/standart_profile.html'