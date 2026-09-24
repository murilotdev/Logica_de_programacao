ct = 0
cp = 0
soma = 0
somap = 0
print('Digite -1 para sair')
while True:
    x = int(input('Digite um número inteiro: '))
    if x == -1:
        break
    elif x % 2 == 0:
        somap = somap + x
        cp = cp + 1
    soma = soma + x
    ct = ct + 1
print('\nTotal de números:', ct)
print('Soma dos números:', soma)
print('Total de números pares:', cp)
print('Soma dos números pares:', somap)
print('Média dos núemros pares', somap / cp)