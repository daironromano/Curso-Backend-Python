from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Documento
from .forms import DocumentoForm

# Create your views here.

# Redirecionamento para rota do advogado e do usuarios

@login_required
def home(request):
    if request.user.groups.filter(name='Advogado').exists():
        return redirect('painel_advogado') # Redicerionamento para o html 'painel_advogado'
    else:
        return redirect('meus_documentos')
    
# ---- VIEWS DO USUÁRIOS ----    
# Identifica qual o tipo de usuário (pu seja, se é advogado)
def is_advogado(user):
    return user.groups.filter(name='Advogado').exists()

@login_required
def meus_documentos(request):
    # Segurança: mostra documentos apenas do usuario em questão
    docs = Documento.objects.filter(dono=request.user)
    return render(request, 'lista_cliente.html', {'docs': docs})

# Carregamento de documentos
def upload_documento(request):
    if request.method == 'POST':
        form = DocumentoForm(request.POST, request.FILES)
        if form.is_valid():
            doc = form.save(commit=False)
            doc.dono = request.user
            doc.save()
            return redirect('meus_documentos')
        else:
            form = DocumentoForm()
    
        return render(request, 'upload.html', {'form': form})
        
# ---- VIEWS DO ADVOGADO ----    
# Renderizer front-end do advogado
@login_required # Aplicando segurança que requer login
@user_passes_test(is_advogado) # Aplica segurança para garantir que é um advogado
def painel_advogado(request):
    docs = Documento.objects.all()
    return render(request, 'painel_advogado.html', {'docs': docs})

@login_required # Aplicando segurança que requer login
@user_passes_test(is_advogado) # Aplica segurança para garantir que é um advogado
def mudar_status(request, id, novo_status):
    doc = get_object_or_404(Documento, pk=id)
    doc.status = novo_status
    doc.save()
    return redirect('painel_advogado')
    