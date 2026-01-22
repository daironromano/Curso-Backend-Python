from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.db.models import Sum, F
from django.template.loader import render_to_string
from django.http import HttpResponse
from weasyprint import HTML
from .models import *
from .serializers import *


# Create your views here.
# API PUBLICA (VALIDAÇÃO DE INGRESSO)
@api_view(['GET']) 
def validar_ingresso(request, codigo_ingresso):
    participante = get_object_or_404(Participantes, codigo_ingresso=codigo_ingresso) # Busca o participante pelo código do ingresso
    return Response({
        'valido': True,
        'participante': participante.nome,
        'categoria': "VIP" if participante.vip else "STANDARD",
    })

# API INTERNA (CONSULTAR PREÇO)
@api_view(['GET'])
def consultar_preco(request, codigo_barras): # Consulta o preço de um produto pelo código de barras
    produto = get_object_or_404(ProdutosLoja, codigo_barras=codigo_barras) # Busca o produto pelo código de barras
    serializer = ProdutosLojaSerializer(produto)
    return Response(serializer.data)
    
# DASHBOARD 
@api_view(['GET'])
def dashboard(request): # Exibe o dashboard com o faturamento total e gráfico de vendas
    faturamento = Vendas.objects.aggregate(
        total = Sum('produto__preco' * F('quantidade'))['total'] or 0
    ) # Calcula o faturamento total

    total_produtos = Vendas.objects.values('produto__nome').annotate(total_vendido=Sum('quauntidade')).order_by('-total_vendido') # Calcula o total vendido por produto

    # Monta a resposta do dashboard
    return Response({
        'faturamento_total': faturamento
        'grafico': {
            'labels': [item['produto__nome'] for item in total_produtos],
            'data': [item['total_vendido'] for item in total_produtos],
        }
    })

# RELATORIO PDF
# Gera um relatório de vendas em PDF para um participante específico
def gerar_relatorio(request, codigo):
    from reportlab.lib.pagesizes import A4 # Importa tamanho A4 para o PDF
    from reportlab.pdfgen import canvas # Importa canvas para gerar o PDF
    from io import BytesIO # Importa BytesIO para criar o PDF na memória
    
    # Buscar o participante
    participante = get_object_or_404(Participantes, codigo_ingresso=codigo)
    # Criar o PDF
    buffer = BytesIO() # Cria um buffer na memória para o PDF
    p = canvas.Canvas(buffer, pagesize=A4) # Cria um canvas para o PDF
    # Conteúdo do PDF
    p.setFont('helvetica', 15)
    p.drawString(100, 750, f'TechSubmmit 2026 - Relatório de Venda')
    p.setFont('helvetica', 13)
    p.drawString(100, 720, f'Participante: {Participantes.nome}')
    p.save() # Salva o PDF no buffer
    buffer.seek(0) # Volta para o início do buffer
    return HttpResponse(buffer.getvalue(), content_type='application/pdf') # Retorna o PDF como resposta HTTP
    
    
    