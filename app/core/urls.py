from django.urls import path

from core.views import *


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('pre-register/', PreRegisterPageView.as_view(), name='pre_register'),
]