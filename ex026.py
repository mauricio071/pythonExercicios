frase = input('Digite uma frase: ').strip().upper()
cont = frase.count('A')
print(f'A letra A apareceu {cont} vezes')
p = frase.find('A') + 1
print(f'A letra A aparece pela primeira vez na posição {p}')
print('A letra A apareceu na posição {} da ultima vez'.format(frase.rfind('A')+1))