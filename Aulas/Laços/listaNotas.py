notas = [7.3, 8.6, 10.0, 5.3, 4.5, 3.5, 7.5, 6.5]

media = 7
aprovado = reprovado = soma_notas = 0

for nota in notas:
    soma_notas += nota
    if nota >= media:
        print(f'Aluno tirou: {nota}\nELE FOI APROVADO!\n')
        aprovado += 1
    else:
        print(f'Aluno tirou: {nota}\nELE FOI REPROVADO!\n')
        reprovado += 1

media_simples = soma_notas/len(notas)
print(f'TOTAL APROVADOS: {aprovado}')
print(f'TOTAL REPROVADOS: {reprovado}')
print(f'MÉDIA: {media_simples}')

