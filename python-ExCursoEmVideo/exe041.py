from random import randint
computador = randint(1, 10)
print('Acabei de pensar em um número de 1 a 10. Tente advinhar qual é. ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais...Tente novamente: ')
        elif jogador > computador:
            print('Menos...Tente novamente: ')
print('Acertou após {} palpites!'.format(palpites))
