from abc import ABC, abstractmethod

class Produto(ABC):
    def __init__(self, nome, preco_base):
        self.nome = nome
        self.preco_base = preco_base

    @abstractmethod
    def calcular_preco_final():
        pass

class ProdutoFisico(Produto):
    def __init__(self, nome, preco_base, custo_frete):
        super().__init__(nome, preco_base)
        self.custo_frete = custo_frete

class ProdutoDigital(Produto):
    def __init__(self, nome, preco_base, taxa_servico):
        super().__init__(nome, preco_base)
        self.taxa_servico = taxa_servico

