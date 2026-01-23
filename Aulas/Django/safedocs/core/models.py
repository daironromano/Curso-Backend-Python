from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Documento(models.Model):
    # Opções de status: identifica qual o status atual do documento
    status_choices = [
        ('PEN', 'Pendente'),
        ('APV', 'Aprovado'),
        ('REJ', 'Rejeitado'),
    ]
    titulo = models.CharField(max_length=100)
    # A pasta 'docs' será criada no momento em que o primeiro arquivo for enviado
    arquivo = models.FileField(upload_to='docs/')
    # Default: Inicia a variável com o valor 'Pendente'
    status = models.CharField(max_length=3, choices=status_choices, default='PEN')
    # Chave Estrangeira: Cria vínculo entre tabelas
    dono = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.titulo


    
    