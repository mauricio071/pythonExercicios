import random

u = input('Jakennn: (digite a sua opção: pedra ou papel ou tesoura): ').strip()
comp = ('pedra', 'papel', 'tesoura')

if u.upper() == 'PEDRA':
    if random.choice(comp) == 'tesoura':
        print('po: tesoura \nAhhh você ganhou')
    elif random.choice(comp) == 'pedra':
        print('po: pedra \nEmpate')
    elif random.choice(comp) == 'papel':
        print('po: papel \nGanhei')
    else:
        print('Opção inválida')
if u.upper() == 'PAPEL':
    if random.choice(comp) == 'pedra':
        print('po: pedra \nAhhh você ganhou')
    elif random.choice(comp) == 'papel':
        print('po: papel \nEmpate')
    elif random.choice(comp) == 'tesoura':
        print('po: tesoura \nGanhei')
    else:
        print('Opção inválida')
if u.upper() == 'TESOURA':
    if random.choice(comp) == 'papel':
        print('po: papel \nAhhh você ganhou')
    elif random.choice(comp) == 'tesoura':
        print('po: tesoura \nEmpate')
    elif random.choice(comp) == 'pedra':
        print('po: pedra \nGanhei')
    else:
        print('Opção inválida')
