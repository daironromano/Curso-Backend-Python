from django.contrib import admin
from .models import Produto

# Register your models here.
"Registrar dados no Banco de Dados"
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'produtor')
    
admin.site.register(Produto, ProdutoAdmin)
