peso = float(input('Insira seu peso: '))
altura = float(input('Insira sua altura: '))
imc = peso / altura ** 2

if imc < 22:
    print(f'Seu IMC é: {imc:.2f}.\nAbaixo do peso.')
elif 22 <= imc <= 27:
    print(f'Seu IMC é: {imc:.2f}.\nÍndice normal.')
elif 27 <= imc <= 29.99:
    print(f'Seu IMC é: {imc:.2f}.\nSobrepeso.')
else:
    print(f'Seu IMC é: {imc:.2f}.\nObesidade.')