from random import randint
from time import sleep

ale = randint(0,5)

print('-=-' * 20)
print('Vou pensar em número eim noossa')
print('-=-' * 20)

n = int(input('Digite um número de 0 a 5: '))
print('Processando....')
sleep(3)

if n == ale:
    print('Parabéns você acertou')
else:
    print(f'Você errou, pois era o número {ale}')