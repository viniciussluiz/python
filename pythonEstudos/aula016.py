# Coleções- Dicionários e Conjuntos
coleta = {'Aedes aegypt' : 32, 'Aedes albopictus' : 22, 'Anopheles darlingi': 14}
print(coleta['Aedes aegypt'])
print(coleta)
del(coleta)['Aedes albopictus']
print(coleta)
coleta['Rhodnius montenegrensis'] = 11
print(coleta)
print(coleta.items())
print(coleta.keys())
print(coleta.values())
coleta2 = {'Anopheles gambiae': 13, 'Anopheles deaneorum': 14}
coleta.update(coleta2)
print(coleta)
for especie, num_especimes in coleta.items():
    print('Espécie: {}/ Número de espécimes coletados: {}'.format(especie, num_especimes))
print('---')

biomeleculas = ('proteína', 'ácidos nucleicos', 'carboidrato', 'lipídeo', 'ácidos nucleicos', 'carboidrato', 'carboidrato', 'carboidrato')
print(set(biomeleculas))
print('---')
c1 = {1,2,3,4,5}
c2 = {3,4,5,6,7}
c3 = c1.intersection(c2)
print(c3)
c4 = c1.difference(c2)
print(c4)
c5 = c2.difference(c1)
print(c5)