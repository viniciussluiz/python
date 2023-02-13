tempo = float(input('Quanto tempo, em horas, você gastou nessa viagem? '))
velocidade = float(input('Qual foi a velocidade média do percurso, em km? '))
distancia = tempo*velocidade
litros_usados = distancia/12
print('Nessa viagem você gastou {} horas com uma velocidade de {}km/h.\n A distância percorrida foi de {}km.\n A quantidade de litros usados pelo seu carro (que faz 12 litros por km) nessa viagem foi de {}l'.format(tempo, velocidade, distancia, litros_usados))