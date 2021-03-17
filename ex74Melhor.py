from random import randint
num = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1,10))
print(f'Os números aleatórios gerados foram ', end='')
for i in num:
    print(i, end=' ')
print(f'\nO maior número foi {max(num)}')
print(f'O menor número foi {min(num)}')
