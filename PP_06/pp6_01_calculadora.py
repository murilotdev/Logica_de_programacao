def conta1(x,y):
    soma = x + y
    return soma
def conta2(x,y):
    sub = x - y
    return sub
def conta3(x,y):
    mul = x * y
    return mul
def conta4(x,y):
    div = x / y
    return div
if __name__ == '__main__':
    x = float(input('Digite um número: '))
    y = float(input('Digite outro número: '))
    z = str(input('[+] Somar [-] Subtrair\n[x] Multiplicar [/] Dividir\n'))
    rtn1 = conta1(x,y)
    rtn2 = conta2(x,y)
    rtn3 = conta3(x,y)
    rtn4 = conta4(x,y)
    if z == '+':
        print('soma:',rtn1)
    elif z == '-':
        print('Subtração:',rtn2)
    elif z == 'x' or z == 'X':
        print('Multiplicação:',rtn3)
    elif z == '/':
        print('Divisão:',rtn4)
    else:
        print('Operação inválida')