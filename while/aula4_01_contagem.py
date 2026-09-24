ct = 0
soma = 0
print('Digite -1 para sair')
while True:
    x = float(input('Digite um número: '))
    if x == -1:
        break
    ct = ct + 1
    soma = soma + x
print('\nTotal de números:', ct, '\nSoma dos números:', soma)