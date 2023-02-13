a = float(input('Qual a altura da sua parede? '))
l = float(input('E a largura? '))
area = a*l
tinta = area/2
print('A parede tem uma área de {:.0f}m2. \nPrecisarão de {} litros de tinta para pintar'.format(area, tinta))