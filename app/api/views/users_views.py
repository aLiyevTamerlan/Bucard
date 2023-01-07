from django.utils.translation import ugettext_lazy as _
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import status, permissions
from rest_framework.response import Response

from api.serializers import UserSerializer
from api.decorators import handle_errors
from users.implemented import create_user
from users.models import User
from pprint import pprint

class CreateUserView(APIView):
    serializer_classs = UserSerializer
    permission_classes = (permissions.AllowAny, )

    @handle_errors
    def post(self, request, *args, **kwargs):
        success = False
        stat = status.HTTP_400_BAD_REQUEST
        user = create_user.create.run(
            args=request.data 
        )
         
        if user.is_success:
            result = self.serializer_classs(user.value[0]).data
            success = True
            stat = status.HTTP_201_CREATED
            # Simple JWT token data
            result['refresh'] = str(user.value[1])
            result['access'] = str(user.value[1].access_token)
        
        elif user.failed_because('not_validated'):
            result = _('Data not validated.')

        elif user.failed_because('user_exists'):
            result = _('User exists.')
        
        elif user.failed_because('repo_error'):
            result = _('Repo error happened.')
        
        else:
            result = _("Unexpected Error.")

        return Response({'success': success, 'result': result}, status=stat)

    

class UserListView(ListAPIView):
    """
    Returns a list of all **active** users in the system.

    """

    serializer_class = UserSerializer
    queryset = User.objects.filter(is_active=True)
    permission_classes = (permissions.IsAuthenticated,)


class UserDetailView(RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.filter(is_active=True)
    lookup_field = 'pk'
    permission_classes = (permissions.IsAuthenticated,)


class LoggedUserView(APIView):
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, )
    
    def get(self, request, *args, **kwargs):
        serializer = UserSerializer(request.user)
        
        return Response(serializer.data)


    def post(self, request, **kwargs):
        return Response(status=status.HTTP_201_CREATED)