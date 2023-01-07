import imp
from rest_framework import serializers

from users.models import User 
from core.models import PreRegister

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = [
            'password',
            'is_superuser',
            'is_staff',
            'groups',
            'user_permissions'
        ]

class UserOverviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'name',
            'surname',
            'email',
            'is_active',
            'date_joined'
        ]

class PreUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=PreRegister
        fields="__all__"