ct = 0
soma = 0
print('Digite -1 para sair')
dic = str(input('Digite o nome da diciplina: '))
while True:
    nota = float(input('Digite a nota do aluno: '))
    if nota == -1:
        break
    soma = soma + nota
    ct = ct + 1
print('\nNota media:', soma/ct, '\nSoma das notas:', soma, '\nDiciplina:', dic)