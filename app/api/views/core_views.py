from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import permissions
from django.utils.translation import ugettext_lazy as _

from api.decorators import handle_errors
from api.serializers import (
    PromoCodeSerializer,
    PricingSerializer,
    CategorySerializer,
    KeywordOverviewSerializer,
)
from core.implemented import check_promo_code, create_pre_user
from core.models import Pricing, Category
from profiles.models import Keyword

class PromoCodeAPIView(APIView):
    serializer_class = PromoCodeSerializer
    permission_classes = (permissions.AllowAny, )

    @handle_errors
    def get(self, request, *args, **kwargs):
        name = request.data.get('name')
        status_code = status.HTTP_400_BAD_REQUEST
        success = False

        promo_code = check_promo_code.check.run(
            name = name
        )

        if promo_code.is_success:
            status_code = status.HTTP_200_OK
            success = True
            result = self.serializer_class(promo_code.value).data

        elif promo_code.failed_because('not_validated'):
            result = 'Not validated'
        
        elif promo_code.failed_because('code_not_exists'):
            result = 'Promo code is not exists'
        
        elif promo_code.failed_because('code_not_active'):
            result = 'Promo code is not active'


        return Response({'success': success, 'result': result}, status=status_code)  
            

class PricingListAPIView(ListAPIView):
    serializer_class = PricingSerializer
    queryset = Pricing.objects.all()
    permission_classes = (permissions.AllowAny, )


class CategoryListAPIView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = (permissions.AllowAny, )


class PreRegistrationAPIView(APIView):
    permission_classes = (permissions.AllowAny, )

    @handle_errors
    def post(self, request, *args, **kwargs):
        r = create_pre_user.create.run(
            email = request.data.get('email'),
            category_name = request.data.get('category')
        )
        message = ''

        if r.is_success:
            message = _('Pre-registration was successful')
            return Response({'success': True, 'message': message}, status=status.HTTP_200_OK)
        
        elif r.failed_because('not_validated'):
            message = _('Not validated')
        
        elif r.failed_because('user_exists'):
            message = _('User exists')
        
        elif r.failed_because('category_not_found'):
            message = _('Category not found')
        
        return Response({'success': False, 'message': message}, status=status.HTTP_400_BAD_REQUEST)


class ListKeywordAPIView(ListAPIView):
    serializer_class=KeywordOverviewSerializer
    queryset=Keyword.objects.all()