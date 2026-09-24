ctp = 0
cts = 0
ctt = 0
ctn = 0
ctb = 0
while True:
    x = int(input('[1] Candidato 1\n[2] Candidato 2\n[3] Candidato 3\n[4] Nulo\n[5] Branco\n[6] Encerrar\n'))
    if x == 6:
        break
    elif x == 1:
        ctp = ctp + 1
    elif x == 2:
        cts = cts + 1
    elif x == 3:
        ctt = ctt + 1
    elif x == 4:
        ctn = ctn + 1
    elif x == 5:
        ctb = ctb + 1
    else:
        print('Valor invalido')
print('Votos para o candidato 01:', ctp)
print('Votos para o candidato 02:', cts)
print('Votos para o candidato 03:', ctt)
print('Votos nulos:', ctn)
print('Votos em branco:', ctb)