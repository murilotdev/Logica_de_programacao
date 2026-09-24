x = float(input('Digite a primeira nota: '))
y = float(input('Digite a segunda nota: '))
media = (x + y) / 2
if media >= 5:
    print(f'Media do aluno: {media:.2f}', '\nAprovado')
else:
    print(f'Media do aluno: {media:.2f}', '\nReprovado')