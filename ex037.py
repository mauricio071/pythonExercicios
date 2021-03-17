n = int(input('Digite um número: '))
con = int(input('Digite o número da opção para converter: \n-1 para binário \n-2 para octal \n-3 para hexadecimal '))

if con == 1:
    print(bin(n)[2:])
elif con == 2:
    print(oct(n)[2:])
elif con == 3:
    print(hex(n)[2:])
else:
    print('Opção inválida')