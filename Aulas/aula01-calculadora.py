# 1: Multiplicação
# 2: Adição
# 3: Subutração

def Calculadora(x, y, n):
    r = 0
    if n == '1':
        r = x * y
    elif n == '2':
        r = x + y
    elif n == '3':
        r = x - y 
    else:
        print('Operação inválida!')
    return r

n1 = float(input('Digite um valor: '))
n2 = float(input('Digite um valor: '))
op = str(input('Escolha a operação: '))
print('='*15)
r = Calculadora(n1, n2, op)
print(f'Valor: {r}')
print('='*15)