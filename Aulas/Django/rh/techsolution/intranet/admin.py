from django.contrib import admin
from .models import Funcionario

# Register your models here.
# --- Modelando painel administrativo --- 
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('user', 'cargo', 'departamento', 'eh_gestor')

admin.site.register(Funcionario, FuncionarioAdmin)