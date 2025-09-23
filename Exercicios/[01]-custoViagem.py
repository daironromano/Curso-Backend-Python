"""

"""

# Menu
print('='*40)
print(f'{"PLANEJADOR DE VIAGENS":^40}')
print('='*40)

# Solicita dados ao usuários
distancia = float(input('Distância [KM/H]: '))
while True: 
    consumo_carro = float(input('Consumo [KM/L]: '))
    if consumo_carro <= 0:
        print('Consumo deve ser maior que zero. Tente novamente.')
    else:
        break
preco_combustivel = float(input('Preço [R$]: '))

# Calcula a quantidade de combustível necessária
litros = distancia / consumo_carro

# Calcula o custo total da viagem
custo_total = litros * preco_combustivel

# Exibindo resultado final
print(f'Custo total da viagem: R$ {custo_total:.2f}')