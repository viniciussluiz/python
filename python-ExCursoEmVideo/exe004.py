l = float(input('Qual a largura da parede? '))
a = float(input('Quanl a altura da parede? '))
area = l*a
tinta = area/2
print('Sua parede tem dimensão de {}x{} e sua área é de {}m2.\n Você gastaria {}l de tinta para pintar a parede'.format(l, a, area, tinta))