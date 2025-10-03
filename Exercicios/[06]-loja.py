from abc import ABC, abstractmethod

class Produto(ABC):
    def __init__(self, nome, preco_base):
        self.nome = nome
        self.preco_base = preco_base

    @abstractmethod
    def calcular_preco_final(self):
        pass

class ProdutoFisico(Produto):
    def __init__(self, nome, preco_base, custo_frete):
        super().__init__(nome, preco_base)
        self.custo_frete = custo_frete

    def calcular_preco_final(self):
        return self.preco_base + self.custo_frete

class ProdutoDigital(Produto):
    def __init__(self, nome, preco_base, taxa_servico):
        super().__init__(nome, preco_base)
        self.taxa_servico = taxa_servico

    def calcular_preco_final(self):
        return self.preco_base + self.taxa_servico

# Saída Esperada
carrinho = []
total = 0
while True:
    tipo = input('[F] - Produto Físico\n[D] - Produto Digital\n[P] - Parar de gastar!\nOpção Escolhida: ').upper()
    if tipo == 'P':
        break

    nome = input('Nome do produto: ')
    preco = float(input('Preço: '))

    if tipo == 'F':
        frete = float(input('Valor do frete: '))
        produto = ProdutoFisico(nome, preco, frete)
    elif tipo == 'D':
        frete = float(input('Taxa de serviço: '))
        produto = ProdutoDigital(nome, preco, frete)
    else:
        print('Opção Inválida!')
        continue
    #Adicionando produtos a lista de carrinho    
    carrinho.append(produto)

print('\n')

for produto in carrinho:
    preco_final = produto.calcular_preco_final()
    print(f'{produto.nome}: R$ {preco_final:.2f}')
    total += preco_final

print(f'\nValor total: {total:.2f}')