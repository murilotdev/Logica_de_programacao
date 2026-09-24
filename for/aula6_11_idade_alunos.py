soma = 0
ct = 0
novo = 99999999999999
velho = 0
cm = 0
for num in range(1,11):
    idade = float(input('Insira a idade do aluno: '))
    soma = soma + idade
    ct = ct + 1
    if idade < novo:
        novo = idade
    if idade > velho:
        velho = idade
    if idade < 18:
        cm = cm + 1
media = soma / ct
print('Soma das idades dos alunos: ', soma)
print('Média das idades dos alunos: ', media)
print('Aluno mais novo: ', novo)
print('Aluno mais velho: ', velho)
print('Aluno menores de idade: ', cm)