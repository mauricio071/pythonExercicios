contI = 0
contS = 0
contM =0
while True:
    idade = int(input('Digite a sua idade: '))
    while True:
        sexo = input('Digite o seu sexo: [M/ F]:')
        if sexo.upper() in 'MF':
            break
    while True:
        cont = input('Deseja continuar? [S/N]')
        if cont.upper() in 'SN':
            break
    if idade >= 18:
        contI += 1
    if sexo.upper() == 'M':
        contS += 1
    if sexo.upper() == 'F' and idade < 20:
        contM += 1
    if cont.upper() == 'N':
        break
print(f'\n{contI} pessoas são maiores de 18 anos')
print(f'{contS} são homens')
print(f'{contM} mulheres tem menos de 20 anos')