from math import sqrt,pow,hypot
ca = float(input('Digite o valor do cateto adjacente: '))
co = float(input('Digite o valor do cateto oposto: '))
#h² = a² + b²
h = sqrt(pow(ca,2) + pow(co,2))
'''Sem usar o import
h = (ca**2 + co**2)**(1/2)
h = hypot(ca,co)'''

print(f'A himpotenusa desse triângulo perfeito é {h:.2f}')