from django import forms

from core.models import PreRegister


class PreRegisterForm(forms.ModelForm):
    class Meta:
        model = PreRegister
        fields = ['email', 'category']