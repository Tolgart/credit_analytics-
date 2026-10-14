from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import CorporateClient

def client_list(request):
    clients = CorporateClient.objects.all()

    return render(request, 'clients/clients_list.html', {'clients': clients})

def client_detail(request, pk):
    client = get_object_or_404(CorporateClient.objects.prefetch_related('financial_statements'), pk=pk)

    return render(request, 'clients/client_detail.html',
                  {'client': client,
                   'financial_statements': client.financial_statements.all()})