from django.db import models
import uuid

# Create your models here.

class Participantes(models.Model):
    codigo_ingresso = models.UUIDField(default=uuid.uuid4, 
                                        editable=False, # Evite que o código seja editável.
                                        unique=True,) # Garante que o código seja único.
    nome = models.CharField(max_length=100)
    vip = models.BooleanField(default=False)
    
    def __str__(self):
        return self.nome
    
class ProdutosLoja(models.Model):
    nome = models.CharField(max_length=100) # Nome do produto
    preco = models.DecimalField(max_digits=10, decimal_places=2) # Preço do produto
    codigo_barras = models.CharField(max_length=13, unique=True) # Código de barras único do produto
    
    def __str__(self):
        return self.nome

class Vendas(models.Model):
    produto = models.ForeignKey(ProdutosLoja, on_delete=models.CASCADE) # Relação com o produto vendido
    quantidade = models.IntegerField(default = 1) # Quantidade vendida
    
    def __str__(self):
        return f"Venda de {self.quantidade} unidade(s) de {self.produto.nome}"