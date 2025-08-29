
def add_tarefa(tarefas):
    titulo = input('Digite o título da tarefa: ')
    tarefas.append({'titulo': titulo, 'concluida': False})

def listar_tarefas(tarefas):
    for i, tarefa in enumerate(tarefas, start=0):
        print(f'{i}ª, {tarefa}')
        
def marcar_concluida(tarefas):
    listar_tarefas(tarefas)

    num = int(input('Qual tarefa marcar: '))
    tarefas[num - 1]['concluida'] = True
    print(f'Tarefa {num} concluída!')

def sair():
    return False

def main():
    tarefas = []
    opcao = {
        '1': add_tarefa(),
        '2': listar_tarefas(),
        '3': marcar_concluida(),
        '4': sair()
    }

    continuar = True
    while continuar:
        print(opcao)
        escolha = input('Qual a sua escolha: ')
        funcoes = opcao.get(escolha)
        if funcoes:
            if funcoes(tarefas) == False:
                continuar == False

