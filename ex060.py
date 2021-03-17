n = int(input('Digite um número: '))
c = n
fat = 1
while c > 0:
    print(f'{c}', end='')
    if c > 1:
        print(' x ', end='')
    else:
        print(' = ', end='')
    fat *= c
    c -= 1
print(fat)

'''n = int(input('Digite um número: '))
fat = 1
for c in range(n, 0, -1):
    fat *= c
print(f'{n}! = {fat}')'''