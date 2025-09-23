"""
CONCEITOS BÁSICOS:
Este exercício aborda conceitos básicos da
programação como condificonais.

if: se (não depende do else)
Ex.: se (condição) == Verdadeiro/Falso: faça algo

else: senão (depende do if)
Ex.: senão for Verdadeiro/Falso: faça esse outro algo

"""

# INPUTS
peso = float(input('Insira seu peso: '))
altura = float(input('Insira sua altura: '))

# TRATAMENTO DOS DADOS
imc = peso / altura ** 2

# CONDICIONAIS
if imc < 22:
    print(f'Seu IMC é: {imc:.2f}.\nAbaixo do peso.')
elif 22 <= imc <= 27:
    print(f'Seu IMC é: {imc:.2f}.\nÍndice normal.')
elif 27 <= imc <= 29.99:
    print(f'Seu IMC é: {imc:.2f}.\nSobrepeso.')
else:
    print(f'Seu IMC é: {imc:.2f}.\nObesidade.')