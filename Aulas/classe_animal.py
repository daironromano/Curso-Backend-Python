class Animal:
    def __init__(self, nome, idade, peso):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.vivo = True
        self.fome = 50

        def comer(self):
            if self.vivo:
                self.fome = 10
                print(f'{self.nome} está comendo!')
            else:
                return f'O animal foi de arrasta!'

        def dormir(self):
            if self.vivo:
                return f'{self.nome} está dormindo'
            else:
                return f'{self.nome} não pode dormir'

        def mover(self):
            pass

        def emitir_som(self):
            if self.vivo:
                return f'{self.nome} emite um som'
            else:
                return f'{self.nome} não pode emitir som'