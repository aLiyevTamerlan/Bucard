import json

from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from drf_yasg.utils import swagger_auto_schema

from users.repository import user_repo
from profiles.repository import profile_repo
from profiles.models import Business
from profiles.implemented import (
    create_business,
    create_pro,
    create_standard,
    create_free,
    fetch_pro,
    fetch_standard,
)
from api.serializers import (
    BusinessProfileSerializer,
    PROProfileOverviewSerializer,
    StandardProfileOverviewSerializer,
    FreeProfileOverviewSerializer
)
from api.decorators import handle_errors


class CreateBusiness(APIView):
    # View for Creating a Business Profile
    serializer_class = BusinessProfileSerializer
    permission_classes = (permissions.IsAuthenticated, )

    @handle_errors
    def post(self, request, *args, **kwargs):        
        success = False
        stat = status.HTTP_400_BAD_REQUEST
        user_id = request.user.id

        r = create_business.create.run(
            user_id=user_id,
            args=request.data
        )

        if r.is_success:
            success = True
            result = self.serializer_class(r.value).data
            stat = status.HTTP_201_CREATED

        elif r.failed_because('not_validated'):
            result = _('Data not validated.')
        
        elif r.failed_because('user_not_exists'):
            result = _('User not exists.')
            
        elif r.failed_because('business_exists'):
            result = _('Business exists.')
        
        elif r.failed_because('repo_error'):
            result = _('Repo error happened.')
        
        else:
            result = _("Unexpected Error.")

        return Response({'success': success, 'result': result}, status=stat)


class BusinessesListAPIView(ListAPIView):
    queryset = Business.objects.all()
    serializer_class = BusinessProfileSerializer
    permission_classes = (permissions.IsAuthenticated,)


class BusinessDetailAPIView(RetrieveAPIView):
    serializer_class = BusinessProfileSerializer
    queryset = Business.objects.all()
    lookup_field = 'id'
    permission_classes = (permissions.IsAuthenticated,)


class CreatePROProfile(APIView):
    serializer_class = PROProfileOverviewSerializer
    permission_classes = (permissions.IsAuthenticated, )

    @handle_errors
    def post(self, request, *args, **kwargs):        
        success = False
        stat = status.HTTP_400_BAD_REQUEST
        user_id = request.user.id

        r = create_pro.create.run(
            user_id=user_id,
            args=request.data
        )

        if r.is_success:
            success = True
            result = self.serializer_class(r.value).data
            stat = status.HTTP_201_CREATED

        elif r.failed_because('not_validated'):
            result = _('Data not validated.')
        
        elif r.failed_because('user_not_exists'):
            result = _('User not exists.')
            
        elif r.failed_because('pro_profile_exists'):
            result = _('PRO profile related user exists.')
        
        elif r.failed_because('repo_error'):
            result = _('Repo error happened.')
        
        else:
            result = _("Unexpected Error.")

        return Response({'success': success, 'result': result}, status=stat)


class RetrievePROProfile(APIView):
    serializer_class = PROProfileOverviewSerializer
    permission_classes = (permissions.IsAuthenticated, )

    @handle_errors    
    def get(self, request, *args, **kwargs):
        success = False
        stat = status.HTTP_400_BAD_REQUEST
        user_id = request.user.id

        r = fetch_pro.apply.run(user_id=user_id)

        if r.is_success:
            success = True
            result = self.serializer_class(r.value).data
            stat = status.HTTP_201_CREATED
        
        elif r.failed_because('not_validated'):
            result = _('Data not validated.')
        
        elif r.failed_because('user_not_exists'):
            result = _('User not exists.')
            
        elif r.failed_because('repo_error'):
            result = _('Repo error happened.')
        
        else:
            result = _("Unexpected Error.")

        return Response({'success': success, 'result': result}, status=stat)


class CreateStandardProfile(APIView):
    serializer_class = StandardProfileOverviewSerializer
    permission_classes = (permissions.IsAuthenticated, )

    @handle_errors
    def post(self, request, *args, **kwargs):        
        success = False
        stat = status.HTTP_400_BAD_REQUEST
        user_id = request.user.id

        r = create_standard.create.run(
            user_id=user_id,
            args=request.data
        )

        if r.is_success:
            success = True
            result = self.serializer_class(r.value).data
            stat = status.HTTP_201_CREATED

        elif r.failed_because('not_validated'):
            result = _('Data not validated.')
        
        elif r.failed_because('user_not_exists'):
            result = _('User not exists.')
            
        elif r.failed_because('standard_profile_exists'):
            result = _('Standard profile related user exists.')
        
        elif r.failed_because('repo_error'):
            result = _('Repo error happened.')
        
        else:
            result = _("Unexpected Error.")

        return Response({'success': success, 'result': result}, status=stat)


class RetrieveStandardProfile(APIView):
    serializer_class = StandardProfileOverviewSerializer
    permission_classes = (permissions.IsAuthenticated, )

    @handle_errors    
    def get(self, request, *args, **kwargs):
        success = False
        stat = status.HTTP_400_BAD_REQUEST
        user_id = request.user.id

        r = fetch_standard.apply.run(user_id=user_id)

        if r.is_success:
            success = True
            result = self.serializer_class(r.value).data
            stat = status.HTTP_201_CREATED
        
        elif r.failed_because('not_validated'):
            result = _('Data not validated.')
        
        elif r.failed_because('user_not_exists'):
            result = _('User not exists.')
            
        elif r.failed_because('profile_not_found'):
            result = _('Standard profile related user not exists.')
        
        else:
            result = _("Unexpected Error.")

        return Response({'success': success, 'result': result}, status=stat)


class CreateFreeProfile(APIView):
    serializer_class =FreeProfileOverviewSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def post(self, request, *args, **kwargs):        
        success = False
        stat = status.HTTP_400_BAD_REQUEST
        user_id = request.user.id

        r = create_free.create.run(
            user_id=user_id,
        )

        if r.is_success:
            success = True
            result = self.serializer_class(r.value).data
            stat = status.HTTP_201_CREATED

        elif r.failed_because('user_id_required'):
            result = _('User id is required.')
        
        elif r.failed_because('user_not_exists'):
            result = _('User not exists.')
        
        elif r.failed_because('profile_exists'):
            result = _('Profile related user exists.')
        
        elif r.failed_because('repo_error'):
            result = _('Repo error happened.')
        
        else:
            result = _("Unexpected Error.")

        return Response({'success': success, 'result': result}, status=stat)