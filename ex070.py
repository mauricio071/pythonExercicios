tot = 0
pro1 = 0
bara = 0
while True:
    nome = input('Digite o nome do produto: ')
    prod = float(input('Digite o preço do produto: '))
    if tot == 0:
        bara = nome
        baraP = prod
    elif prod < baraP:
        bara = nome
        baraP = prod
    if prod > 1000:
        pro1 += 1
    tot += prod
    cont = input('Deseja continuar? [S/N]:')
    if cont.upper() == 'N':
        break
print(f'O valor total gasto: {tot:.2f}')
print(f'{pro1} produtos custam mais de R$1000')
print(f'O produto mais barato é {bara} que custa R${baraP}')