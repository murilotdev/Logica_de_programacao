def conta1(x):
    fat = 1
    for num in range(1,x+1):
        fat = fat * num
    return fat
if __name__ == '__main__':
    x = int(input('Digite um número: '))
    rtrn = conta1(x)
    print(rtrn)

