vel = float(input('Qual a velocidade do carro, em km, nesse trecho? '))
if vel > 80:
    print('Você foi multado!')
    print('Terá que pagar R${} de multa.'.format((vel - 80) * 7))
else:
    print('Você está andando na velocidade certa.')