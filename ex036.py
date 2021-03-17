vc = float(input('Digite o valor da casa: '))
sal = float(input('Digite o valor do seu salário: '))
anop = int(input('Em quantos anos você irá pagar o empréstimo: '))

emp = vc / (anop * 12)

if emp <= sal * 0.30:
    print(f"Você terá que pagar R${emp:.2f} em {anop} ano(s)")
else:
    print('Empréstimo negado.')