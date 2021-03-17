from random import randint
v = 0

while True:
    jogador = int(input('Vamos brincar de par ou ímpar!! Digite um número!!'))
    computador = randint(0, 10)
    total = computador + jogador
    tipo = ''
    if pi == 'p'.upper:
        if total % 2 ==0:
            print('Você venceu')
            v+= 1
        else:
            print('VOce perdeu')
            break
    elif pi == 'i'.upper:

print(f'Você venceu {cont} vezes')