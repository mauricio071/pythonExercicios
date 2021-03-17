dia = int(input('Quantos dias alugados?: '))
rodad = float(input('Quantos Km rodados? '))
preco = 60 * dia + rodad * 0.15
print(f"O valor do aluguel é : R$ {preco}")