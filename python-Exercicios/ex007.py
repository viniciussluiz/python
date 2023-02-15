#Exercícios Coleções - Lista
lista = []
for _ in range(1, 6):
    valor = int(input('Digite o valor: '))
    lista.append(valor)
print(lista)

soma = 0
for i in range(len(lista)):
 print(lista[i])
 soma += lista[i]
print('Soma', soma)

import numpy as np
np.array(lista).sum()
print(np.array(lista).sum())
