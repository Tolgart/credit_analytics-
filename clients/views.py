from django.shortcuts import render, get_object_or_404

from .models import CorporateClient, FinancialStatement
from .services import get_client_financial_summary, get_periods_for_analysis

def client_list(request):
    clients = CorporateClient.objects.all()

    return render(request, 'clients/clients_list.html', {'clients': clients})

def client_detail(request, pk):
    client = get_object_or_404(CorporateClient.objects.prefetch_related('financial_statements'), pk=pk)

    periods_for_analysis = get_periods_for_analysis(client)

    return render(request, 'clients/client_detail.html',
                  {
                   'client': client,
                   'financial_statements': periods_for_analysis,
                   'financial_summary': get_client_financial_summary(periods_for_analysis['current_period']),
                   },
                  )