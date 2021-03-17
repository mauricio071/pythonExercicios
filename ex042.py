l1 = float(input('Digite o lado 1: '))
l2 = float(input('Digite o lado 2: '))
l3 = float(input('Digite o lado 3: '))

if l1 + l2 > l3 and l2 + l3 > l1 and l1 + l3 > l2:
    print('Forma um triângulo', end=' ')
    if l1 == l2 and l1 == l3:
        print('Equilátero')
    elif (l1 == l2 and l1 != l3) or (l2 == l3 and l2 != l1) or (l3 == l1 and l3 != l2):
        print('Isósceles')
    else:
        print('Escaleno')
else:
    print('Não forma um triângulo')
