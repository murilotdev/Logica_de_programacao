soma = 0
ct = 0
x = int(input('Digite o primeiro número inteiro: '))
y = int(input('Digite o segundo número inteiro: '))
if x < y:
    for num in range(x,y+1,1):
        ct = ct + 1
        soma = soma + num
        print(num)
    print('\nCrescente')
    print('Total de números:', ct)
    print('Soma dos números:', soma)
    print('Média dos números:', soma / ct)
elif x > y:
    for num in range(x,y-1,-1):
        ct = ct + 1
        soma = soma + num
        print(num)
    print('\nDecrescente')
    print('Total de números:', ct)
    print('Soma dos números:', soma)
    print('Média dos números:', soma / ct)
else:
    print('Os valores são iguais')
