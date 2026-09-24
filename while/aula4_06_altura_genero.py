ct = 0
soma = 0
menor = 9999999999999
maior = 0
ctm = 0
ctf = 0
somam = 0
somaf = 0
menorm = 99999999999999
maiorm = 0
menorf = 99999999999999
maiorf = 0
print('Digite -1 para sair')
while True:
    g = int(input('[1] Masculino\n[2] Feminino\n'))
    if g == -1:
        break
    x = float(input('Digite a altura: '))
    if x < menor:
        menor = x
    if x > maior:
        maior = x
    if g == 1:
        ctm = ctm + 1
        somam = somam + x
        if x < menorm:
            menorm = x
        if x > maiorm:
            maiorm = x
    if g == 2:
        ctf = ctf + 1
        somaf = somaf + x
        if x < menorf:
            menorf = x
        if x > maiorf:
            maiorf = x
    soma = soma + x
    ct = ct + 1
print('\nTotal de pessoas:', ct)
print('Soma de todas as alturas:', soma)
print('Maior pessoa:', maior)
print('Menor pessoa:', menor)
print('\nTotal de Homens:', ctm)
print('Soma das alturas dos homens:', somam)
print('Maior Homem:', maiorm)
print('Menor Homem:', menorm)
print('\nTotal de Mulheres:', ctf)
print('Soma das alturas das mulheres:', somaf)
print('Maior Mulher:', maiorf)
print('Menor Mulher:', menorf)