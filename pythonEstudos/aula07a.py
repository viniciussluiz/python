n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
d = n1/n2
m = n1*n2
di = n1//n2
e = n1**n2
print('A soma entre entre eles é {}. \nO produto é {}. \nE a divisão é {:.3f}.'.format(s, m, d), end=' ')
print('A divisão inteira é {} e a exponenciação é {}'.format(di, e))
