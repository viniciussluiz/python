distancia = float(input('Qual a distância da sua viagem, em km? '))
print('Sua viagem tendo {}km de distância, então:'.format(distancia))
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print('O preço da sua passagem será de R${:.2f}'.format(preço))