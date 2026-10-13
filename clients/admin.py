from django.contrib import admin
from clients.models import CorporateClient


@admin.register(CorporateClient)
class CorporateClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'inn', 'industry', 'is_active')
    list_filter = ('is_active', 'industry')
    search_fields = ('name', 'inn')
    list_per_page = 10
