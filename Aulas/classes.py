class ContaBancaria:
    # Caracteríticas = Atributos
    def __init__(self, numero, titular, saldo=0, limite=1000):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.transacoes = []

    # Comportamento = Métodos
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
        print('Seu saldo foi atualizado!')
        
    def sacar():
        pass
    def saldo():
        pass
contaDairon = ContaBancaria("001", "Dairon", "2000", "500")
