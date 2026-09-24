ct = 0
ar = 0
ap = 0
soma = 0
print('Digite -1 para sair')
while True:
    x = float(input('Digite um numero: '))
    if x == -1:
        break
    if x > 4:
        ap = ap + 1
    elif x < 5:
        ar = ar + 1
    ct = ct + 1
    soma = soma + x
    media = soma / ct
print('Alunos aprovados:', ap, '\nAlunos reprovados:', ar, '\nMédia dos alunos:', media)