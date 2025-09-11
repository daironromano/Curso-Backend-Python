#Função para adicionar uma nova tarefa
def add_tarefa(tarefas):
    titulo = input('Digite a tarefa: ')
    tarefas.append({'titulo': titulo, 'concluida': False})

#Função para listar as tarefas
def listar_tarefas(tarefas):
    for i, tarefa in enumerate(tarefas, start=0):
        print(f"{i+1}ª Tarefa: {tarefa['titulo']}\nConcluída: {'Não concluída' if not tarefa['concluida'] else 'Concluída'}\n")

#Função para marcar como concluída as tarefas    
def marcar_concluida(tarefas):
    listar_tarefas(tarefas)
    try:
        num = int(input('Qual tarefa marcar: '))
        if 1 <= num <= len(tarefas):
            tarefas[num - 1]['concluida'] = True
            print(f'Tarefa {num} concluída!')
        else:
            print('Número de tarefa inválido!')
    except ValueError:
        print('Entrada inválida. Digite um número.')

def remover_tarefa(tarefas):
    listar_tarefas(tarefas)
    remover = input('Qual tarefa deseja remover: ')
    for i, tarefa in enumerate(tarefas):
        if tarefa['titulo'].lower() == remover.lower:
            removida = tarefa.pop(i)
            print(f'Tarefa: {removida['titulo']} removida! ')
            return  
        print('Tarefa não encontrada.')

def sair():
    return False

def main():
    tarefas = []
    #dicionário fazendo referência as funções
    opcao = {
        '1': add_tarefa,
        '2': listar_tarefas,
        '3': marcar_concluida,
        '4': remover_tarefa,
        '5': sair
    }

    continuar = True
    while continuar:
        print(f'======= Menu =======')
        print(f'1) Adicionar Tarefa \n2) Listar Tarefas \n3) Marcar Concluído \n4) Remover Tarefa\n5) Sair')
        escolha = input('Qual a sua escolha: ')
        funcao_escolhida = opcao.get(escolha)
        if funcao_escolhida:
            if escolha == '5':
                continuar = funcao_escolhida()
            else:
                funcao_escolhida(tarefas)
        else:
            print('Opção inválida. Tente novamente.')

main()