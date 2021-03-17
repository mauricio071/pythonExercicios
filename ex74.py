from random import randint
num1 = (randint(0, 10),)
num2 = (randint(0, 10),)
num3 = (randint(0, 10),)
num4 = (randint(0, 10),)
num5 = (randint(0, 10),)
total = num1 + num2 + num3 + num4 + num5
cont = 0
mai = 0
for i in range(0, len(total)):
    if cont == 0:
        men = total[i]
        cont += 1
    if cont == 0:
        mai = total[i]
        cont += 1
    elif total[i] < men:
        men = total[i]
    elif total[i] > mai:
        mai = total[i]
print(f'Os números sorteados foram: {total}')
print(f'O maior número foi {mai}')
print(f'O menor número foi {men}')