from django.urls import path
from . import views

urlpatterns = [
    path('', views.client_list, name='client_list'),
    path('<int:pk>/', views.client_detail, name='client_detail'),
    path('create/', views.client_create, name='client_create'),
]