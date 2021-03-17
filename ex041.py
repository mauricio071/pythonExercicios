ano = int(input('\033[1;35;42mDigite o seu ano de nascimento:\033[m'))
ant = 2020;

ida = ant - ano

if ida <= 9:
    print('Mirim')
elif ida <= 14:
    print('Infantil')
elif ida <= 19:
    print('Junior')
elif ida <= 20:
    print('Senior')
else:
    print('Master')