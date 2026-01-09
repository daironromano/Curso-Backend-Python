from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PedidoForms
from .models import Prato, ItemPedido

# Create your views here

def home_pedido_rapido(request):
    pratos_disponiveis = Prato.objects.filter(ativo=True)
    
    if request.method == 'POST': #verificando se o método da requisição é POST
        form = PedidoForms(request.POST) 
        
        if form.is_valid(): #validando formulário com o método is_valid()
            novo_pedido = form.save(commit=False) #salvando o formulário sem enviar para o banco de dados
            novo_pedido.status = 'PENDENTE'  #definindo o status do novo_pedido como PENDENTE
            novo_pedido.save()
            
            prato_selecionado = form.cleaned_data['prato_escolhido']
            
            ItemPedido.objects.create(
                pedido=novo_pedido,
                prato=prato_selecionado,
                quantidade=1
            )
            
            return redirect('home')
        else:
            messages.error(
                request, 
                f'Pedido #{novo_pedido.id} não pode ser criado'                
            )
            
    else:
        form = PedidoForms()
        
    return render(request,  'home_pedido.html', {'form': form,})
        