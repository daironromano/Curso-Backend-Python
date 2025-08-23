print('=== JOGO DE ADIVINHAÇÃO === ')

palpite = 0
num_secreto = 48

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