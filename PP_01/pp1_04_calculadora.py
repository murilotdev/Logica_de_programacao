x = float(input('Digite um número : '))
y = float(input('Digite outro número : '))
z = float(input('(1) Soma\n(2) Subtração\n(3) Multiplicação\n(4) Divisão\n'))
soma = x + y
sub = x - y
mult = x * y
div = x / y
if z == 1:
    print(soma)
elif z == 2:
    print(sub)
elif z == 3:
    print(mult)
elif z == 4:
    print(div)
else:
    print('Operação invalida')