from django.contrib import admin
from .models import Documento

# Register your models here.

@admin.register(Documento) # Essa linha exibe o campo 'Documento' no painel administrativo.
class DocumentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'dono', 'status', 'ver_arquivo') # ver_arquivo: função será configurada aidna
    search_fields = ('titulo', 'dono__username')

    # definindo função ver_arquivo
    @admin.display(description='Arquivo')
    def ver_arquivo(self, obj):
        return "Sim" if obj.arquivo else "Não"
    
