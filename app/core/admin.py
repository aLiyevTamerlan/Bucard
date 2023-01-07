from django.contrib import admin

from .models import (
    Image, 
    Category, 
    PromoCode,
    PricingField,
    Pricing,
    PreRegister,    
)


class PricingFieldInline(admin.StackedInline):
    model = PricingField
    extra = 0


@admin.register(Pricing)
class PricingAdmin(admin.ModelAdmin):
    inlines = [
        PricingFieldInline
    ]

admin.site.register(Image)
admin.site.register(Category)
admin.site.register(PromoCode)
admin.site.register(PreRegister)

