lista = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('-'*30)
print(f'{"Listagem de preços":>23}')
print('-'*30)
for i in range(0, len(lista)):
    if i % 2 == 0:
        print(lista[i],end='')
    else:
        print(f'R${lista[i]:.>30}')


print('-'*30)