ano = int(input('Digite o ano de nascimento: '))
ant = 2020;

if ant - ano < 18:
    print(f'Ainda vai se alistar, falta {18 - (ant - ano)} anos')
elif ant - ano == 18:
    print('Ta na hora de alistar')
else:
    print(f'''Passou do prazo, faz {(ant - ano) - 18} anos
{ano + 18}''')