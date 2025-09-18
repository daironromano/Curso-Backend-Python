class Animal:
    def __init__(self, nome, idade, peso):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.vivo = True
        self.fome = 50

    def comer(self):
        if self.vivo:
            self.fome += 10
            print(f'{self.nome} está comendo!')
        else:
            return f'O animal foi de arrasta!'

    def dormir(self):
        if self.vivo:
            self.fome -= 10
            return f'{self.nome} está dormindo'
        else:
            return f'{self.nome} não pode dormir'

    def mover(self):
        if self.vivo:
            return f'{self.nome} pode se mover'
        else:
            return f'{self.nome} foi de arrasta!@'

    def emitir_som(self):
        if self.vivo:
            return f'{self.nome} emite um som'
        else:
            return f'{self.nome} não pode emitir som'
            
animal = Animal("João", 150, 52.6)
print(animal.nome)
animal.dormir()