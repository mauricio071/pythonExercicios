n = int(input('Digite um número: '))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print(f'\033[33m', end=' ')
        tot+= 1
    else:
        print('\033[31m', end=' ')
    print(f'{c}', end=' ')
print(f'\nO número {n} foi divisível {tot} vezes')

if tot == 2:
    print('É primo')
else:
    print('Não é primo')