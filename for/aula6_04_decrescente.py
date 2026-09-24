soma = 0
ct = 0
for num in range(7,0,-1):
    soma = soma + num
    ct = ct + 1
    print(num)
print('Total de números:', ct)
print('Soma dos números:', soma)
print('Média dos números:', soma/ct)