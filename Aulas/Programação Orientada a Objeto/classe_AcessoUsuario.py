import functools

context_user = {"user_logado": None}

def login_requirido(funcao_original_para_decorada):
    @functools.wraps(funcao_original_para_decorada)
    def wrapper(*args, **kwargs):
        # Verificação 
        if context_user["user_logado"] is None:
            print('Acesso negado!')
            return
        else:
            print(f'Acesso permitido para: {funcao_original_para_decorada.__name__}')
            return funcao_original_para_decorada(*args, **kwargs)
    return wrapper
        
@login_requirido
def painel_usuario(nome_usuario):
    print(f'Bem-vindo ao seu painel: {nome_usuario}') 
    return 'Página do Painel'       

def pagina_inicial():
    print('Bem-vindo a página pública')

pagina_inicial()

#Simulando login
context_user["user_logado"] = "Maria"
r_painel2 = painel_usuario("Maria")
