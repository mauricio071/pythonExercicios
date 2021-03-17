while True:
    n = int(input('Digite um número: '))
    if n < 0:
        break
    print('-' * 20)
    for i in range(1, 11):
        print(f'{n} x {i} = {n*i}')
    print('-' * 20)
print('Programa da tabuada encerrada')