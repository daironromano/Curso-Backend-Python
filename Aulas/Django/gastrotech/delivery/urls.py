from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_pedido_rapido, name='home'),
]