'''co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hipotenusa = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}.'.format(hipotenusa))'''

import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hipotenusa = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))

