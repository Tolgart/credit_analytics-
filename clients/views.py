from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse

from .models import CorporateClient

def client_list(request):
    clients = CorporateClient.objects.all()

    return render(request, 'clients/clients_list.html', {'clients': clients})
