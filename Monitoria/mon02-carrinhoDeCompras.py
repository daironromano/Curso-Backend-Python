print('========= SUPERMERCADO =========')
carrinho = []

print('COMANDOS DISPONÍVEIS: \n[1] ADICIONAR\n[2] LISTAR\n[3] FINALIZAR')
comando = input('Digite o comando: ').upper()

if comando == 'FINALIZAR':
    print('Compra finalizada.')
    breakpoint
    
elif comando == 'ADICIONAR':
    nome_produto = input('Nome do produto: ')
    preco_produto = input(f'Preço de {nome_produto}: ')
    
    produto = {
        'nome': nome_produto,
        'preco': preco_produto
    }
    print(f'{nome_produto} adicionado ao carrinho')
    carrinho.append(produto)
elif comando == 'LISTAR':
    if len(carrinho) == 0:
        print('O carrinho está vazio!')
    else:
        print('Total de items:', len(carrinho))
        print(carrinho)

else:
    print('Comando inválido!')