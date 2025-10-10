from abc import ABC, abstractmethod

class Personagem(ABC):
    def __init__(self, nome, vida, ataque_base):
        self.nome = nome
        self._vida = vida
        self._ataque_base = ataque_base

    def receber_dano(self, dano):
        self._vida -= dano
        if self._vida < 0: # CORREÇÃO: Usar _vida
            self._vida = 0 # CORREÇÃO: Usar _vida
        print(f'{self.nome} recebeu {dano} de dano.\n Vida restante: {self._vida}')
    
    def esta_vivo(self):
        return self._vida > 0

    @abstractmethod
    def atacar(self, alvo): # CORREÇÃO: Adicionar self
        pass

class Guerreiro(Personagem):
    def __init__(self, nome, vida, ataque_base, furia_inicial=50):
        super().__init__(nome, vida, ataque_base)
        self.__furia = furia_inicial # CORREÇÃO: Usar furia_inicial

    def atacar(self, alvo):
        dano = self._ataque_base
        print(f'{self.nome} ataca {alvo.nome} com um golpe de espada.')
        alvo.receber_dano(dano)
    
    def ataque_especial(self, alvo):
        custo_furia = 20
        dano_extra = self._ataque_base * 1.5

        if self.__furia >= custo_furia:
            self.__furia -= custo_furia
            print(f'{self.nome} executa um ATAQUE ESPECIAL! (-{custo_furia} de Fúria)')
            alvo.receber_dano(dano_extra) # CORREÇÃO: Aplicar o dano
        else:
            print(f'{self.nome} não tem fúria suficiente')

class Mago(Personagem):
    def __init__(self, nome, vida, ataque_base, mana_inicial=75):
        super().__init__(nome, vida, ataque_base)
        self.__mana = mana_inicial # CORREÇÃO: Usar mana_inicial

    def atacar(self, alvo):
        custo_mana = 15
        dano_magia = self._ataque_base * 1.2

        if self.__mana >= custo_mana:
            self.__mana -= custo_mana
            print(f'{self.nome} lança uma magia em {alvo.nome}! (-{custo_mana} de Mana)')
            alvo.receber_dano(dano_magia) # CORREÇÃO: Aplicar o dano da magia
        else:
            print(f'{self.nome} está sem mana suficiente para lançar a magia.') # CORREÇÃO: Mensagem de erro

# Simulação da Batalha 

guerreiro = Guerreiro("Conan, o Bárbaro", 100, 15)
mago = Mago("Merlin, o Enigmático", 70, 20)

print("--- INÍCIO DA BATALHA ---")
turno = 1

while guerreiro.esta_vivo() and mago.esta_vivo():
    print(f"\n===== TURNO {turno} =====")

    if turno % 3 == 0:
        guerreiro.ataque_especial(mago)
    else:
        guerreiro.atacar(mago)
    
    if mago.esta_vivo():
        mago.atacar(guerreiro)
    
    turno += 1
    
print("\n--- FIM DA BATALHA ---")
if guerreiro.esta_vivo():
    print(f"Vencedor: {guerreiro.nome}!")
elif mago.esta_vivo():
    print(f"Vencedor: {mago.nome}!")
else:
    print("Ambos caíram!")