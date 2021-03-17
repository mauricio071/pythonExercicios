from random import shuffle

nom1 = input('Digite o primeiro nome: ')
nom2 = input('Digite o segundo nome: ')
nom3 = input('Digite o terceiro nome: ')
nom4 = input('Digite o quarto nome: ')

lista = [nom1,nom2,nom3,nom4]
shuffle(lista)

print(f'A ordem vai ser: {lista}')