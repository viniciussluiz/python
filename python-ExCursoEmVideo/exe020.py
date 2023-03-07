from random import choice
numero = int(input('Tente acertar o número que a máquina vai escolher de 1 a 5: '))
lista = [1, 2, 3, 4, 5]
escolhido = choice(lista)
print('O número que a máquina escolheu foi {}'.format(escolhido))
if numero == escolhido:
    print('Parabéns, vc acertou!')
else:
    print('Você errou!')

