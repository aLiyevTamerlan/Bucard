from django.urls import path
from profiles.views import *



urlpatterns = [
    path('standart-profile/', StandartPageView.as_view(), name='standart_profile'),
    path('pro-profile/', ProPageView.as_view(), name='pro_profile'),
    path('free-profile/', FreePageView.as_view(), name='free_profile'),
    path('company-profile/', CompanyPageView.as_view(), name='company_profile'),
]