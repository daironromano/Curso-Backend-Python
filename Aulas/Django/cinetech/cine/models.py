from django.db import models

# Create your models here (banco de dados)

# Primeira classe de filmes
class Filmes(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.nome

