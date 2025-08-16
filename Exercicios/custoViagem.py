# Menu
print('='*40)
print(f'{"PLANEJADOR DE VIAGENS":^40}')
print('='*40)

# Solicita dados ao usuários
distancia = float(input('Distância [KM/H]: '))
consumo_carro = float(input('Consumo [KM/L]: '))
preco_combustivel = float(input('Preço [R$]: '))

# Calcula a quantidade de combustível ncessária
litros = distancia / consumo_carro

# Calcula o custo total da viagem
custo_total = litros * preco_combustivel

# Exibindo resultado final
print(f'Custo total da viagem: {custo_total:.2f}')