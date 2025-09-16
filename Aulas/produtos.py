class Produto():

    def __init__(self, nome: str, preco: float, estoque: int):
        #RF01 
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
        print(f'Produto {self.nome} criado com o preço de {self.preco} e estoque de {self.estoque} unidades.')

    def aplicar_desconto(self, perctual_desconto: float):
        #RF02
        desconto = self.preco * (perctual_desconto / 100)
        novo_preco = self.preco - desconto

        #RFN01
        if novo_preco < 0:
            self.preco = 0.0
            print(f'[INFO]: Desconto de {perctual_desconto} aplicado em {self.nome}')
        else:
            self.preco = novo_preco
            print(f'[INFO]: Desconto de {perctual_desconto} aplicado em {self.nome}')

    #RF03
    def verificar_estoque(self):
        return self.estoque > 0

# Criando objetos 
notebook = Produto("Asus", 4.500, 0)
celular = Produto("Iphone 16", 7.500, 12)

# Verificação de estoque
print(f'O produto: {notebook.nome} está em estoque? {'Sim' if notebook.verificar_estoque() else 'Não'}')
print(f'O produto: {celular.nome} está em estoque? {'Sim' if notebook.verificar_estoque() else 'Não'}')