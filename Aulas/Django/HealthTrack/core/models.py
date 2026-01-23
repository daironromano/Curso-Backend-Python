from django.db import models
# Com ele conseguimos pegar os dados do usuário
from django.contrib.auth.models import User

# Create your models here.

class Paciente(models.Model):
    # Relação 1:1
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    cep = models.CharField(max_length=8, blank=True)
    endereco = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.user.username
   