from django.contrib import admin

from .models import Business, ProProfile, StandardProfile, FreeProfile, Keyword
from core.models import Service, Product

# Register your models here.

class BusinessProductInline(admin.StackedInline):
    model = Product
    fk_name = 'business'
    extra = 1


class BusinessServiceInline(admin.StackedInline):
    model = Service
    fk_name = 'business'
    extra = 1


@admin.register(ProProfile)
class PROProfileAdminCustom(admin.ModelAdmin):
    pass


class BusinessProfileCustomAdmin(admin.ModelAdmin):
    inlines = [
        BusinessServiceInline,
        BusinessProductInline,
    ] 


admin.site.register(Business ,BusinessProfileCustomAdmin)
admin.site.register(StandardProfile)
admin.site.register(FreeProfile)
admin.site.register(Keyword)