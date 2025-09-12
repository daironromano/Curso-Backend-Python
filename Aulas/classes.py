class ContaBancaria:
    # Caracteríticas = Atributos
    def __init__(self, numero, titular, saldo=0, limite=1200):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.transacoes = []

    # Comportamento = Métodos
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.transacoes.append(f"Depósito de R$ {valor:.2f} realizado!")
            return "Seu saldo foi atualizado com sucesso!"
        else:
            return "Valor de depósito inválido!"

    def sacar(self, valor):
        if valor > 0 and valor <= (self.saldo + self.limite):
            self.saldo -= valor
            self.transacoes.append(f"Saque de R${valor:.2f } realizado!")
            return "Seu saque foi realizado com sucesso!"
        else:
            return "Valor do saque indisponível!"
        
    def consultar_saldo(self):
        return f"Valor atual: R$ {self.saldo}"


contaDairon = ContaBancaria("001", "Dairon", 2000)
contaFilite = ContaBancaria("002", "Filite", 1500, 2100)

print(contaDairon.depositar(600))
print(contaDairon.consultar_saldo())

