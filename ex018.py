from math import sin,cos,tan,radians
angulo = float(input('Digite o valor de um ângulo: '))
seno = sin(radians(angulo))
cos = cos(radians(angulo))
tag = tan(radians(angulo))
print(f'O seno é: {seno:.2f} \ncosseno é: {cos:.2f} \ntangente é: {tag:.2f}')