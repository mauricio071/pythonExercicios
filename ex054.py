from datetime import date
m = 0
n = 0
atual = date.today().year
for c in range(1, 8):
    idade = atual - ano
    ano = int(input('Digite o ano do seu nascimento: '))
    if idade >= 21:
        m += 1
    else:
        n += 1
print(f'\n{m} pessoas são/é de maioridade\n{n} pessoas não são/é de maior')