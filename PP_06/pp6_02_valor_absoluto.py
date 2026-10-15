def conta(x):
    if x < 0:
        res = x * -1
    else:
        res = x
    return res
if __name__ == '__main__':
    x = int(input('Digite um número para ter o valor absoluto: '))
    rtrn = conta(x)
    print(rtrn)
