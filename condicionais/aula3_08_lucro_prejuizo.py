z = str(input('Digite o nome do produto: '))
x = float(input('Digite o valor de compra: '))
y = float(input('Digite o valor de venda: '))
dif = x - y
if x > y:
    print('\nProduto:', z, '\nvalor de compra:', x, '\nvalor de venda:', y)
    print('\nTeve Prejuizo de:', dif)
elif x < y:
    print('\nProduto:', z, '\nvalor de compra:', x, '\nvalor de venda:', y)
    print('\nTeve Lucro de:', dif)
else:
    print('\nProduto:', z, '\nvalor de compra:', x, '\nvalor de venda:', y)
    print('Saiu no 0 a 0')