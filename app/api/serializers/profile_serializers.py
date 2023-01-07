from rest_framework import serializers

from profiles.models import Business, StandardProfile, ProProfile, FreeProfile, Keyword
from .user_serializers import UserSerializer, UserOverviewSerializer
from .core_serializers import ProductSerializer


class BusinessProfileSerializer(serializers.ModelSerializer):
    managers = UserSerializer(many=True, read_only=True)
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Business
        fields = [
            'name', 
            'description', 
            'managers',
            'about', 
            'products',
            'slug',
            'type',
            'mobile_number',
            'fax_number',
            'email_address',
            'fb',
            'linkedin',
            'ig',
            'vk',
        ]   


class FreeProfileOverviewSerializer(serializers.ModelSerializer):
    user = UserOverviewSerializer(read_only=True)

    class Meta:
        model = FreeProfile
        fields = [
            'user'
        ]


class PROProfileOverviewSerializer(serializers.ModelSerializer):
    user = UserOverviewSerializer(read_only=True)
    keywords=serializers.StringRelatedField(many=True)
    class Meta:
        model = ProProfile
        fields = [
            'user',
            'about',
            'phone_number',
            'slug',
            'profile_image',
            'qr_code',
            'keywords',
        ] 


class StandardProfileOverviewSerializer(serializers.ModelSerializer):
    user = UserOverviewSerializer(read_only=True)

    class Meta:
        model = StandardProfile
        fields = [
            'user',
            'about',
            'phone_number',
            'slug',
            'profile_image',
            'qr_code',
            'private_account',
            'profile_link',
        ]

class KeywordOverviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Keyword
        fields="__all__"