valor = int(input('Qual o valor a retirar: '))
v50 = 0
v20 = 0
v10 = 0
v1 = 0

v50 = valor // 50
valor %= 50
print(f'{v50} cédulas de R$50')

v20 = valor // 20
valor %= 20
print(f'{v20} cédulas de R$20')

v10 = valor // 10
valor %= 10
print(f'{v10} cédulas de R$10')

v1 = valor // 1
valor %= 1
print(f'{v1} cédulas de R$1')