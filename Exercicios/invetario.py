inventario = []

def mostrarMenu():
    print("\n=== CONTROLE DE INVENTÁRIO ===")
    print('1. Adicionar item')
    print('2. Remover item')
    print('3. Listar inventário')
    print('4. Sair')

while True:
    mostrarMenu()
    opcao = input('Escolha uma opção: ').strip()

    match opcao:
        case "1":  # Adicionar item
            nome = input('Nome do item: ').strip()
            if not nome:
                print('Nome não pode ser vazio.')
                continue
        
            while True:
                qtd_str = input('Quantidade: ').strip()
                if not qtd_str.isdigit():
                    print('Informe um número inteiro válido.')
                    continue
                quantidade = int(qtd_str)
                break

            inventario.append({"nome": nome, "quantidade": quantidade})
            print(f"Item '{nome}' adicionado com quantidade {quantidade}.")

        case "2":  # Remover item
            alvo = input('Nome do item a remover: ').strip()
            if not alvo:
                print('Nome não pode ser vazio.')
                continue

            idx = next((i for i, it in enumerate(inventario)
                        if it["nome"].lower() == alvo.lower()), None)

            if idx is None:
                print(f"Item '{alvo}' não encontrado.")
            else:
                removido = inventario.pop(idx)
                print(f"Item '{removido['nome']}' removido com sucesso.")

        case "3":  # Listar inventário
            if not inventario:
                print("Inventário vazio.")
            else:
                print("\n-- Itens no inventário --")
                for i, item in enumerate(inventario, start=1):
                    print(f"{i}. {item['nome']} — {item['quantidade']}")

        case "4":  # Sair
            print("Saindo... Até mais!")
            break

        case _:  # Opção inválida
            print("Opção inválida. Tente novamente.")
