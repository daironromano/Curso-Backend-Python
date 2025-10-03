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
p1 = ProdutoFisico("Livro Python", 50, 15)
p2 = ProdutoFisico("Caneca", 30, 10)
p3 = ProdutoDigital("E-book Django", 40, 5)
p4 = ProdutoDigital("Curso Online", 200, 20)

carrinho = [p1, p2, p3, p4]

total = 0
for produto in carrinho:
    preco_final = produto.calcular_preco_final()
    print(f"{produto.nome}: R$ {preco_final:.2f}")
    total += preco_final

print(f"\nValor total da compra: R$ {total:.2f}")