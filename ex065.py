conf = 'S'
s = 0
cont = 0
ma = 0
me = 0
num = 0
while conf.upper() != 'N':
    n = int(input('Digite um número: '))
    if cont == 0:
        ma = n
        me = n
    elif n > ma:
        ma = n
    elif n < me:
        me = n
    s += n
    cont += 1
    num += 1
    conf = input('Deseja continuar? (S/N) ')
print(f'Você digitou {num} números')
print(f'O maior núemero entre eles foi {ma}')
print(f'O menor número entre eles foi {me}')
print(f'A média entre eles é {s / cont}')