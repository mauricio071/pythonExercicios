dis = float(input('Digite a distância da sua viagem pelo carro em Km: '))

if dis <= 200:
    print(f'O valor da passagem é: {dis * 0.50:.2f} reais')
else:
    print(f'O valor da passagem é: {dis * 0.45:.2f} reais')
