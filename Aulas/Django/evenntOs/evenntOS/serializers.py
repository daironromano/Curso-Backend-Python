from rest_framework import serializers
from .models import Participantes, ProdutosLoja, Vendas

class ParticipantesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participantes
        fields = [
            'nome',
            'vip',
            'codigo_ingresso',
        ]
        
class ProdutosLojaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProdutosLoja
        fields = [
            'nome',
            'precos',
            'codigo_barras',
        ]

class VendasSerializer(serializers.ModelSerializer):
    produto_nome = serializers.CharField(source='produto.nome', read_only=True)
    produto_preco = serializers.DecimalField(source='produto.preco',max_digits=10, decimal_places=2, read_only=True)
    
    class Meta:
        model = Vendas
        fields = [
            'id',
            'quantidade',
            'produto_nome',
            'produto_preco',            
        ]
        