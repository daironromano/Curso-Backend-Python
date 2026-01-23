from django.contrib import admin
from .models import Especialidade, Medico, Prontuario
from django.db import models

# Register your models here.

@admin.register(Medico)
class MedicoAdmin(admin.ModelAdmin):
    list_display = ('user', 'crm', 'especialidade')

admin.site.register(Especialidade)

@admin.register(Prontuario)
class ProntuarioAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'medico', 'data', 'receita')
    
    actions = ['adicionar_obs_padrao']
    @admin.action(description='Adicionar observação padrão')
    def adicionar_obs_padrao(self, request, queryset):
        update = queryset.update(descricao=models.F('descricao') + '\n Retorno sugerido em 30 dias.')
        self.message_user(request, f'{update} Prontuários atualizados com sucesso.')
        