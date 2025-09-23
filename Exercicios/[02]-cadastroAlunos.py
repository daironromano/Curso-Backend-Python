# cadastro_alunos.py

def cadastrar(alunos):
    nome = input('Digite seu nome: ')
    curso = input('Digite seu curso: ')

    try:
        matricula = int(input('Digite sua matrícula (apenas números): '))
    except ValueError:
        print('Matrícula inválida! Apenas números.')
        return

    aluno = {
        "nome": nome,
        "curso": curso,
        "matricula": matricula
    }

    alunos.append(aluno)
    print('Aluno cadastrado com sucesso!')


def listar(alunos):
    if not alunos:
        print("Nenhum aluno cadastrado ainda.")
        return

    print("\n--- Lista de Alunos ---")
    for aluno in alunos:
        print(f"Nome: {aluno['nome']} | Matrícula: {aluno['matricula']} | Curso: {aluno['curso']}")


def buscar(alunos):
    try:
        matricula = int(input("Digite a matrícula do aluno: "))
    except ValueError:
        print("Matrícula inválida! Digite apenas números.")
        return

    for aluno in alunos:
        if aluno["matricula"] == matricula:
            print(f"Aluno encontrado: {aluno['nome']} | Curso: {aluno['curso']}")
            return
    
    print("Aluno não encontrado.")


def sair(_):
    print("Saindo do sistema. Até logo!")
    exit()


def main():
    alunos = []  # lista criada dentro da main

    funcoes = {
        "1": cadastrar,
        "2": listar,
        "3": buscar,
        "4": sair
    }

    while True:
        print("\n--- Cadastro de Alunos Simplificado ---")
        print("1. Cadastrar Novo Aluno")
        print("2. Listar Alunos Cadastrados")
        print("3. Buscar Aluno por Matrícula")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        funcao = funcoes.get(opcao)
        if funcao:
            funcao(alunos)  
        else:
            print("Opção inválida. Tente novamente.")


main()
