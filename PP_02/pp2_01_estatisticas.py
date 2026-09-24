ct = 0
soma = 0
print('Digite -1 para sair')
while True:
    x = float(input('Digite um numero: '))
    if x == -1:
        break
    ct = ct + 1
    soma = soma + x
    media = soma / ct
print('Valores digitados:', ct, '\nSoma dos valores:', soma, '\nMédia dos valores:', media)
