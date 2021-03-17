from random import choice
nom1 = input('Digite o primeiro nome: ')
nom2 = input('Digite o segundo nome: ')
nom3 = input('Digite o terceiro nome: ')
nom4 = input('Digite o quarto nome: ')

lista = [nom1,nom2,nom3,nom4]
escolhido = choice(lista)

print(f'O nome sorteado foi: {escolhido}')