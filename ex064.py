n = 0
s = 0
cont = 0
while n != 999:
    n = int(input('Digite um número: [Digite 999 para sair]'))
    if n != 999:
        s += n
        cont += 1
print(f'A soma deu {s} em {cont} tentativas')