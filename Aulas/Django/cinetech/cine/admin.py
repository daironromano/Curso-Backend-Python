from django.contrib import admin
from .models import Filmes

# Register your models here (Interface de administração)

@admin.register(Filmes)
class FilmeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco')
    search_fields = ('nome',)
    list_editable = ('preco',)

