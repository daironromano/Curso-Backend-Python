'''

Aplicando conceitos de programação orientada a objetos, com ênfase
em encapsulamento, pois foi a aula do dia.

'''

from abc import ABC, abstractmethod

class ContaBancaria(ABC): #classe abstrata
    def __init__(self, saldo_inicial=0):
        self.__saldo = saldo_inicial #aplicando encapsulamento

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f'Depósito de R${valor:.2f} realizado!')

    def get_saldo(self): ##MÉTODO GETTER
        return self.__saldo

    @abstractmethod
    def sacar(self, valor):
        pass

class ContaCorrente(ContaBancaria): #Classe concreta
    def __init__(self, saldo_inicial=0, taxa_operacao=1.50):
        super().__init__(saldo_inicial)
        self.__taxa_operacao = taxa_operacao

    def sacar(self, valor):
        custo_total = valor - self.__taxa_operacao
        if valor > 0 and self.get_saldo() >= custo_total:
            novo_saldo = self.get_saldo() - custo_total
            self._ContaBancaria__saldo() = novo_saldo
            print(f'Saque de R${valor:.2f} realizado!\nSaldo restante R$ {self.get_saldo()}')
        else:
            print('Saque não realizado. Saldo insuficiente!')

class ContaPoupanca(ContaBancaria): #Classe concreta
    def __init__(self, saldo_inicial=0, taxa_juros=0.1):
        super().__init__(saldo_inicial)
        self.__taxa_juros = taxa_juros
    
    def sacar(self, valor):
        if valor > 0 and self.get_saldo() >= valor:
            novo_saldo = self.get_saldo() - valor
            self._ContaBancaria__saldo() = novo_saldo
            print(f'Saque de R${valor:.2f} realizado!\nSaldo restante R$ {self.get_saldo()}')
        else:
            print('Saque não realizado. Saldo insuficiente!')

    def aplicar_juros(self):
        juros = self.get_saldo() * self.__taxa_juros
        self.depositar(juros)
        print(f'Juros de R$ {juros:.2f} aplicado!')

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.__contas = []
    
    def adicionar_contas(self, conta: ContaBancaria):
        self.__contas.append(conta)
        print(f'Conta adicionada: {type(conta).__name__}')