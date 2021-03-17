menu = 0
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
while menu != 5:
    menu = int(input('''--- Digite a opção desejada ---
[1]somar
[2]multiplicar
[3]maior
[4]novos números
[5]sair do programa '''))

    if menu == 1:
        print(n1 + n2)
    elif menu == 2:
        print(n1 * n2)
    elif menu == 3:
        if n1 > n2:
            print(n1)
        else:
            print(n2)
    elif menu == 4:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo núemro: '))
    else:
            print('Comando inválido')
print('FIM')

