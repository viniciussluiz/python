#Módulos úteis- Biblioteca random e biblioteca time
import random
print(random.random())
print(random.randint(1, 10))
print(random.randrange(0, 10, 2))
print(random.randrange(0, 20, 3))
x = ['K', 'd', '13', '34-j', 'x']
print(x)
print(random.choice(x))
print('---')
import time as tm
print(tm.time())
antes = tm.time()
lista = []
for i in range(0, 10000):
    lista.append(i)
depois = tm.time()
intervalo = depois - antes
print(f'Tempo: {intervalo} segundos')
print('Finalizando...')
tm.sleep(3)
print('...')
tm.sleep(2)
print('Até a próxima')