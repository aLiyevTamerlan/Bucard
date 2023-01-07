from rest_framework import permissions
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path, include

from . import views

schema_view = get_schema_view(
   openapi.Info(
      title="API",
      default_version='v1',
      description="Buca Endpoints provided by Back-end",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="hi@ughur.me"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

user_patterns = [
    path(
        'create/',
        views.CreateUserView.as_view(),
        name='create_user'
    ),
]

profile_patterns = [
    path(
        'business/create/',
        views.CreateBusiness.as_view(),
        name='create_business_profile'
    ),
    path(
        'business/detail/<id>/',
        views.BusinessDetailAPIView.as_view(),
        name='details_of_business_profile'
    ),
    path(
        'business/all/',
        views.BusinessesListAPIView.as_view(),
        name='all_businesses'
    ),
    path(
        'pro/create/',
        views.CreatePROProfile.as_view(),
        name='create_pro_profile'
    ),
    path(
        'pro/detail/',
        views.RetrievePROProfile.as_view(),
        name='detail_of_pro_profile'  
    ),
    path(
        'standard/create/',
        views.CreateStandardProfile.as_view(),
        name='create_standard_profile'
    ),
    path(
        'standard/detail/',
        views.RetrieveStandardProfile.as_view(),
        name='detail_of_standard_profile'  
    ),
    path(
        'free/create/',
        views.CreateFreeProfile.as_view(),
        name='create_free_profile'
    ),
    path(
        'keywords/',
        views.ListKeywordAPIView.as_view(),
        name='keywords-list'
    ),
]

core_patterns = [
    path(
        'promo-code/', 
        views.PromoCodeAPIView.as_view(), 
        name='promo_code_check'
    ),
    path(
        'pricing/', 
        views.PricingListAPIView.as_view(), 
        name='pricing-list'
    ),
    path(
        'categories/',
        views.CategoryListAPIView.as_view(),
        name='categories-list'
    ),
    path(
        'pre-registration/',
        views.PreRegistrationAPIView.as_view(),
        name='pre-registration'
    ),
    
]

urlpatterns = [
    path('user/', include(user_patterns)),
    path('profile/', include(profile_patterns)),
    path('core/', include(core_patterns)),
    # Token
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
