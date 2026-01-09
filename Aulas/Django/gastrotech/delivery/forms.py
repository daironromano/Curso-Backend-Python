from django import forms
from .models import Pedido, Prato

class PedidoForms(forms.ModelForm):
    prato_escolhido = forms.ModelChoiceField(
        queryset=Prato.objects.filter(ativo=True),
        empty_label='Selecione um prato',
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Qual será o pedido de hoje?'
        )
    
class Meta:
    model = Pedido
    fields = ['cliente_nome', 'cliente_endereco']
    
    widgets = {
        'cliente_nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome Completo'}),
        'cliente_endereco': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Endereço Completo', 'rows': 3}),      
    }
    
    labels = {
        'cliente_nome': 'Nome do Cliente',
        'cliente_endereco': 'Endereço de Entrega',
    }

