from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Filmes
from .forms import ExpectadorForm

# Create your views here.

# Sessão do carrinho
def adicionar_ao_pedido(request, filme_id):
    sacola = request.session.get('ingressos_selecionados', {})
    filme_id_str = str(filme_id)
    sacola[filme_id_str] = sacola.get(filme_id_str, 0) + 1
    request.session['ingressos_selecionados'] = sacola
    request.session.modified = True
    messages.sucess(request, 'Ingresso adicionado ao carrinho')
    return redirect('index')

def limpar_sacola(request):
    if 'ingressos_selecionados' in request.session:
        del request.session['ingressos_selecionados']
    return redirect('ver_sacola')
    
# Rascunho & Checkout 
def ver_sacola(request):
    

# Controle de Acesso