from django.contrib import admin
from django.contrib import messages
from .models import Prato, Pedido, ItemPedido
# Register your models here.

admin.site.site_header = "Administração Gastrotech"
admin.site.site_title = "Gastrotech"
admin.site.index_title = "Painel de Administração Gastrotech"

@admin.register(Prato)
class PratoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'categoria', 'estoque', 
                    'preco', 'calcular_faturamento', 'ativo')
    list_editable = ('preco', 'estoque', 'ativo')
    list_filter = ('categoria', 'ativo')
    search_fields = ('nome',)
    
    @admin.display(description='Faturamento Estimado')
    def calcular_faturamento(self, obj):
        faturamento = obj.preco * obj.estoque
        return f'R$ {faturamento}'
    
class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido
    extra = 1
    autocomplete_fields = ['prato']
    
@admin.register(Pedido) 
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente_nome', 'status', 'data_pedido', 'atendente')
    
    list_filter = ('status', 'data_pedido')
    inlines = [ItemPedidoInline]
    readonly_fields = ('data_pedido', 'atendente')
    fieldsets = (
        ('Dados do Cliente', {
            'fields': ('cliente_nome', 'cliente_endereco')
        }),
    
        ('Controle Interno', {
            'classes': ('collapse',),
            'fields': ('status', 'data_pedido', 'atendente')
        }),
    )
    
    @admin.action(description='Marcar pedidos como entregues')
    def marcar_como_entregue(self, request, queryset):
        atualizados = queryset.update(status='ENTREGUE')
        
        self.message_user(
            request,
            f'{atualizados} pedidos foram marcados como entregues.',
            messages.SUCCESS
        )
        
    actions = [marcar_como_entregue]
    