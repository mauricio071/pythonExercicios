largura = float(input('Digite a largura em metros: '))
altura = float(input('Digite a altura em metros: '))
area = largura * altura
tinta = area / 2
print('Para parede com a área de {}m², vai precisar de {}L de tintas.'.format(area, tinta))