x = float(input('Digite um valor: '))
if x > 0:
    dobro = x * 2
    print(x, 'é positivo\nDobro:', dobro)
elif x < 0:
    triplo = x * 3
    print(x, 'é negativo\nTriplo:', triplo)
else:
    print(x, 'é nulo')