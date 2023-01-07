from django.views.generic import TemplateView


class CompanyPageView(TemplateView):
    template_name = 'user-profiles/company_profile.html'