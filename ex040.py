n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

med = (n1 + n2) / 2

if med < 5:
    print('Reprovado')
elif med >= 5 and med < 7:
    print('Recuperação')
else:
    print('Aprovado')