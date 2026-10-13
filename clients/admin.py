from django.contrib import admin
from clients.models import CorporateClient, FinancialStatement


@admin.register(CorporateClient)
class CorporateClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'inn', 'industry', 'is_active')
    list_filter = ('is_active', 'industry')
    search_fields = ('name', 'inn')
    list_per_page = 10

@admin.register(FinancialStatement)
class FinancialStatementAdmin(admin.ModelAdmin):
    list_display = ('client', 'period', 'revenue', 'ebitda', 'net_debt', 'equity', 'report_date')
    list_filter = ('client', 'period', 'report_date')