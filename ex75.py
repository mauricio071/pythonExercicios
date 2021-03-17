num = (int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite mais um número: ')), int(input('Digite o último número: ')))
print(f'Você digitou os valores {num}')
print(f'Você digitou o 9: {num.count(9)} vezes')
if 3 in num:
    print(f'Você digitou o 3: {num.index(3) + 1}ª posição')
else:
    print(f'Você não digitou nenhum valor 3')
print('Os valores pares digitados foram: ', end='')
for i in num:
    if i % 2 == 0:
        print(i, end=' ')

