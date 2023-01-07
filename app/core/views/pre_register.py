from django.views.generic import FormView
from django.contrib import messages

from core.forms import PreRegisterForm
from core.repository import core_repository


class PreRegisterPageView(FormView):
    template_name = 'registration/pre_register.html'
    form_class = PreRegisterForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            'categories': core_repository.get_categories()
        }
        return context

