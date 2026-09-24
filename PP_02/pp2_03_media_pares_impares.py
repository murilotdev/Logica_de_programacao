ct = 0
impar = 0
par = 0
soma = 0
somap = 0
somai = 0
print('Digite 0 para sair')
while True:
    x = float(input('Digite um numero: '))
    if x == 0:
        break
    if x % 2 == 0:
        par = par + 1
        somap = x + somap
    elif x % 2 == 1:
        impar = impar + 1
        somai = x + somai
    ct = ct + 1
    soma = soma + x
mediap = somap / par
madiai = somai / impar
print('Média dos números pares:', mediap, '\nMédia dos números ímpares:', madiai)
print('Números totais:', ct, '\nSoma de todos os núemros:', soma)


