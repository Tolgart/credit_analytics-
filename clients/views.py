from django.shortcuts import render, get_object_or_404, redirect

from .models import CorporateClient
from .forms import CorporateClientForm
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

def client_create(request):
    if request.method == 'POST':
        form = CorporateClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = CorporateClientForm()

    return render(request, 'clients/client_form.html', {'form': form})


def client_update(request, pk):
    client = get_object_or_404(CorporateClient, pk=pk)
    if request.method == 'POST':
        form = CorporateClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client_detail', pk=pk)
    else:
        form = CorporateClientForm(instance=client)

    return render(request, 'clients/client_form.html', {'form': form})


def client_delete(request, pk):
    client = get_object_or_404(CorporateClient, pk=pk)
    if request.method == 'POST':
        client.delete()
        return redirect('client_list')

    return render(request, 'clients/client_confirm_delete.html', {'client': client})
