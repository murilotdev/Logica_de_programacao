ct = 0
x = int(input('Digite um valor para saber a tabuada: '))
for num in range(x,(x*10)+1,x):
    ct = ct + 1
    print(ct, 'x', x, '=', num)