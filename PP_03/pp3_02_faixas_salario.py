ct = 0
soma = 0
menosmin = 0
maismin = 0
maisdez = 0
print('Digite -1 para sair')
while True:
    x = float(input('Digite o sálario do funcionário: '))
    if x == -1:
        break
    if x < 5000:
        menosmin = menosmin + 1
    if x > 4999 and x < 10000:
        maismin = maismin + 1
    if x >= 10000:
        maisdez = maisdez + 1
    ct = ct + 1
    soma = soma + x
print('Funcionários que ganham menos de 5 salários mínimos:', menosmin)
print('Funcionários que estão na faixa de cinco:', maismin)
print('Funcionários que ganham dez ou mais salários mínimos:', maisdez)
print('valor total da folha de pagamento da empresa:', soma)

