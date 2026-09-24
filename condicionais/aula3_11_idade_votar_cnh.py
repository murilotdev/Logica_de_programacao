nome = str(input('Digite seu nome: '))
x = int(input('Digite o ano do seu nascimento: '))
idade = 2026 - x
if idade >= 18:
    print('\nNome:', nome, '\nAno de nascimento:', x, '\nIdade:', idade, 'anos\n', 'Pode votar', '\nPode dirigir')
elif idade >= 16 and idade < 18:
    print('\nNome:', nome, '\nAno de nascimento:', x, '\nIdade:', idade, 'anos\n', 'Pode votar', '\nNão pode dirigir')
elif idade < 16 and idade < 18:
    print('\nNome:', nome, '\nAno de nascimento:', x, '\nIdade:', idade, 'anos\n', 'Não Pode votar', '\nNão pode dirigir')
