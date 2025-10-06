from abc import ABC, abstractmethod

class Personagem(ABC):
    def __init__(self, nome, vida, ataque_base):
        self.nome = nome
        self._vida = vida
        self._ataque_base = ataque_base

    def receber_dano(self, dano):
        return dano - self._vida if self._vida > 0 else "Não é possível causar dano!"
    
    def esta_vivo(self):
        return True if self._vida > 0 else "Foi de arrasta!"

    @abstractmethod
    def atacar(alvo):
        pass