ver = 'S'
t = 10
while ver.upper() != 'N':
    a1 = float(input('Digite o primeiro termo: '))
    r = float(input('Digite a razão: '))
    cont = 1
    while cont <= t:
        print(a1, end='')
        if cont < t:
            print(' -> ', end='')
        else:
            print('')
        a1 += r
        cont += 1
    ver = input('Deseja continuar e acrescentar o termo? (S/N)')
    if ver.upper() != 'N':
     t += int(input('Digite a quantidade de termos que irá acrescentar: '))
print('Fim')

