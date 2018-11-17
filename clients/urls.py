from django.urls import path

from . import views

app_name = 'clients'

urlpatterns = [
    path('', views.ListCreateClient.as_view(), name='client_list'),
    path(
        '<pk>',
        views.RetrieveUpdateDestroyClient.as_view(),
        name='client_detail'),
]
