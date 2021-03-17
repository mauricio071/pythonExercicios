num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    v = int(input('Digite um número de 0 até 20: '))
    if v >= 0 and v <= 20:
        break
    print('Digite novamente')
print(f'Você digitou o número {num[v]}')