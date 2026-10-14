from django.shortcuts import render, get_object_or_404

from .models import CorporateClient, FinancialStatement

def client_list(request):
    clients = CorporateClient.objects.all()

    return render(request, 'clients/clients_list.html', {'clients': clients})

def client_detail(request, pk):
    client = get_object_or_404(CorporateClient.objects.prefetch_related('financial_statements'), pk=pk)
    financial_statements = client.financial_statements.all()

    current_period_financial_statements = financial_statements.first()

    if current_period_financial_statements:
        current_year = int(current_period_financial_statements.report_date.year)
        current_month = current_period_financial_statements.report_date.month
        current_day = current_period_financial_statements.report_date.day

        try:
            full_last_year_financial_statements = client.financial_statements.get(report_date__day=31, report_date__month=12, report_date__year=current_year-1)
            sply_financial_statements = client.financial_statements.get(report_date__day=current_day, report_date__month=current_month, report_date__year=current_year-1)
        except FinancialStatement.DoesNotExist:
            full_last_year_financial_statements = None
            sply_financial_statements = None
    else:
        full_last_year_financial_statements = None
        sply_financial_statements = None

    return render(request, 'clients/client_detail.html',
                  {'client': client,
                   'financial_statements': (sply_financial_statements, full_last_year_financial_statements, current_period_financial_statements),
                   },
                  )