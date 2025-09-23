print("----------- CALCULADORA DE DESCONTOS -----------")
preco = float(input('Preço R$: '))
porcentagem = float(input('Desconto %: '))

valor_desconto = (preco * porcentagem) / 100
preco_final = preco - valor_desconto

print(f'Desconto: {valor_desconto}')
print(f'Preço Final: {preco_final}')