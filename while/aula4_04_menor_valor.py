soma = 0
ct = 0
menor = 999999999999999
while True:
    x = int(input('Digite um número inteiro: '))
    if x == -1:
        break
    elif x < menor:
        menor = x
    ct = ct + 1
    soma = soma + x
if ct > 0:
    print('\nTotal de números:', ct)
    print('Soma dos números:', soma)
    print(f'Média dos valores {soma / ct:.2f}')
    print('Menor número:', menor)
else:
    print('Não foi digitado nenhum valor.')