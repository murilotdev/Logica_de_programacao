um = 0
dois = 0
tres = 0
quatro = 0
cinco = 0
seis = 0
print('Megasena')
import random
for num in range(1,61,1):
    sort = random.randint(1,6)
    if sort == 1:
        um = um + 1
    elif sort == 2:
        dois = dois + 1
    elif sort == 3:
        tres = tres + 1
    elif sort == 4:
        quatro = quatro + 1
    elif sort == 5:
        cinco = cinco + 1
    elif sort == 6:
        seis = seis + 1
    print(sort)
print(seis, cinco, quatro, tres, dois, um)