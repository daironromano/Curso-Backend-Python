from random import randint

print('=== JOGO DE ADIVINHAÇÃO === ')
print('ESCOLHA O NÚMERO DE 1 A 20')

palpite = 0
num_secreto = randint(1, 20)

while palpite != num_secreto:
    palpite_str = input('Qual seu palpite: ')
    if palpite_str.isdigit():
        palpite = int(palpite_str)

        if palpite > num_secreto:
            print('Número muito alto.')
        elif palpite < num_secreto:
            print('Número muito baixo')
    else:
        print('Valor inválido.')

print(f'Você acertou: {num_secreto}')