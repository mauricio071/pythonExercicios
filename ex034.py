salario = float(input('Digite o valor do seu salário: '))

if salario <= 1250:
    print(f'O seu salário com 15% de aumento será: {salario * 1.15:.2f} reais')
else:
    print(f'O seu salário com 10% de aumento será: {salario * 1.10:.2f} reais')
