# Operador condicional
5 > 3
if 5 > 3:
    print('5 é maior que 3')
#print('teste')

if 5 > 6:
    print('5 é maior')
else:
    print('5 não é maior')

n = 9
if n == 4:
    print('n é igual a 4')
else:
    if n == 3:
        print('n é igual a 3')
    else:
        print('n não é igual a 4 e nem a 3')
x = 2
y = 4
if (x > 1) and (y % 2 == 0):
    print('x é maior que 1 e y é par')
else:
    print('Uma ou nenhuma das condições foram satisfeitas')