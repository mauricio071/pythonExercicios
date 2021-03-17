p = float(input('Digite o seu peso: '))
h = float(input('Digite a sua altura: '))

imc = p / (pow(h,2))

if imc < 18.5:
    print('Abaixo do peso')
elif imc < 25:
    print('Peso ideal')
elif imc < 30:
    print('Sobrepeso')
elif imc < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')