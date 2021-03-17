a1 = float(input('Digite o primeiro termo de um número: '))
r = float(input('Digite a razão da PA: '))
cont = 1
a10 = 0

while cont <= 10:
    print(f'{a10}', end='')
    if cont < 10:
        print(' -> ', end='')
    a10 += r
    cont += 1

