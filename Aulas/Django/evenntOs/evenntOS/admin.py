from django.contrib import admin
from .models import Participantes, ProdutosLoja, Vendas

# Register your models here.


@admin.register(Participantes)
class ParticipantesAdmin(admin.ModelAdmin):
    list_display = ('nome', 'vip', 'codigo_ingresso')

admin.site.register(ProdutosLoja)
admin.site.register(Vendas)