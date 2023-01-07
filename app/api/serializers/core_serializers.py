from rest_framework import serializers

from core.models import (
    Product, 
    Service, 
    PromoCode,
    PricingField,
    Pricing,
    Category,
)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__' 


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class PromoCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PromoCode
        fields = [
            'name', 
            'discount_percentage', 
            'start_date', 
            'expiration_date', 
            'limit'
        ]


class PricingFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = PricingField
        fields = [
            'created_at',
            'title'
        ]


class PricingSerializer(serializers.ModelSerializer):
    profile_type = serializers.SerializerMethodField()
    features = serializers.SerializerMethodField()

    class Meta:
        model = Pricing
        fields = [
            'monthly_price',
            'yearly_price',
            'profile_type',
            'features',
        ]
    
    def get_profile_type(self, obj):
        return obj.choice

    def get_features(self, obj):
        return [PricingFieldSerializer(s).data for s in obj.fields.all()]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude=["pricing"]




