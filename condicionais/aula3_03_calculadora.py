x = float(input('Digite um valor: '))
y = float(input('Digite um valor: '))
z = float(input('[1] Somar\n[2] Subtrair\n[3] Multiplicar\n[4] Dividir\n'))
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
    print('Operação inválida')
