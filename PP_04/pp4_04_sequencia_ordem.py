ct = 0
num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
if num1 < num2:
    for num in range(num1,num2,1):
        print(num)
        ct = ct + 1
elif num1 > num2:
    for num in range(num1,num2,-1):
        print(num)
        ct = ct + 1
else:
    print('Números iguais')
print('\nTotal de números:', ct)