ct = 0
soma = 0
menor = 9999999999999999
maior = 0
maiorcin = 0
print('Digite [0] para sair')
while True:
    x = float(input('Digite um valor: '))
    if x == 0:
        break
    if x > maior:
        maior = x
    if x < menor:
        menor = x
    if x >= 50:
        maiorcin = maiorcin + 1
    ct = ct + 1
    soma = soma + x
    media = soma/ct
print('Quantidade de valores digitados:', ct)
print('A soma dos valores digitados:', soma)
print('A média aritmética dos valores digitados:', media)
print('O maior valor digitado:', maior)
print('O menor valor digitado:', menor)
print('Quantidade de valores digitados maior ou igual a 50:', maiorcin)