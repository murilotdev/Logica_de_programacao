soma = 0
ca = 0
cr = 0
ct = 0
for num in range(1,6):
    x = float(input('Digite a nota: '))
    if x >=5:
        ca = ca + 1
        ct = ct + 1
    elif x < 5:
        cr = cr + 1
        ct = ct + 1
    soma = soma + x
print('Alunos reprovados:', cr)
print('Alunos aprovados:', ca)
print('Soma das notas', soma)
print('Média das notas', soma/ct)