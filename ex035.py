r1 = float(input('Digite o valor da reta1: '))
r2 = float(input('Digite o valor da reta2: '))
r3 = float(input('Digite o valor da reta3: '))

if r1 + r2 >= r3 and r2 + r3 >= r1 and r1 + r3 >= r2:
    print('Forma um triângulo')
else:
    print('Não forma um triângulo')