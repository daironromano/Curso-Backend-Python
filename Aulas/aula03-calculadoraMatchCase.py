num1 = int(input('Digite um valor: '))
op = str(input('Digite a operação: '))
num2 = int(input('Digite um valor: ')) 

match op:
    case '+':
        r = num1 + num2
        print(r)
    case '-':
        r = num1 - num2
        print(r)
    case '/':
        if num2 == 0:
            print('Não existe divisão por zero.')
        else:
            r = num1 / num2 
            print(r)
    case '*':
        r = num1 * num2
        print(r)
    case _:
        print('Opção inválida.')