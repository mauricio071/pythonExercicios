v = float(input('Digite a velocidade do carro: '))
if v > 80:
    print(f'Tem que pagar a multa. O valor será de {(v - 80)*7:.2f} reais')
print('Tenha ótimo dia!. Dirija com segurança')