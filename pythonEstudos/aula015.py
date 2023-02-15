# Coleções - Tuplas e Listas

tupla = ('Homo sapiens', 'Canis familiares', 'Felis catus')
tupla[0]
# Homo sapiens
tupla.index('Canis familiares')
# 1
for elemento in tupla:
    print(elemento)
print('---')

l1 = ['Homo sapiens', 'Canis familiares', 'Felis catus']
l2 = ['Xenopus laevis', 'Ailuropoda melanoleuca']
l3 = l1 + l2
print(l3)
print('---')
l2_2 = l2 * 2
print(l2_2)
print('--')
print(l1[0:3])
l1.append('Gorila gorila')
print(l1)
l1.remove('Felis catus')
print(l1)
print('---')

for item in l2_2:
    print(item)