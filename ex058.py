from random import randint

cont = 0
comp = randint(0, 10)
play = 11
while comp != play:
    play = int(input('Digite um número entre 0 a 10: '))
    cont += 1
    if play != comp:
        print('Tente de novo')
    else:
        print(f'Acertou! em {cont} tentativas')
print('Fim')