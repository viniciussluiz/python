def leitura():
    tempo = float(input('Digite o tempo: '))
    velocidade = float(input('Digite a velocidade: '))
    return tempo, velocidade

def calcula_distancia(tempo, velocidade):
    return tempo * velocidade

def calcula_litros(distancia):
    return distancia / 12

def imprime(tempo, velocidade, distancia, litros):
    print('Tempo: ', tempo)
    print('Velocidade: ', velocidade)
    print('Distância: ', distancia)
    print('Litros: ', litros)

t, v = leitura()
d = calcula_distancia(t, v)
l = calcula_litros(d)
imprime (t, v, d, l)
