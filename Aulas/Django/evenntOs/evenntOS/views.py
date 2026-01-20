from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.db.models import Sum, F

from .models import Participantes, ProdutosLoja, Vendas
from .serializers import ParticipantesSerializer, ProdutosLojaSerializer, VendasSerializer

# Create your views here.