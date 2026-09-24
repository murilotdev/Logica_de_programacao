soma = 0
ct = 0
x = int(input('Digite o primeiro número inteiro: '))
y = int(input('Digite o segundo número inteiro: '))
for num in range(x,y+1,1):
    print(num)
    ct = ct + 1
    soma = soma + num
print('Total de números:', ct)
print('Soma dos números:', soma)
print('Média dos números:', soma/ct)