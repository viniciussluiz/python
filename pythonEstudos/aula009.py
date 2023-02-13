# Manipulação de strings
a = 'casaco'
print(a)
maiuscula = a.upper()
print(maiuscula)
minuscula = maiuscula.lower()
print(minuscula)
#Caso você queira apenas a primeira letra maiuscula
capital = a.capitalize()
print(capital)
metade_palavra = a[0:3]
print(metade_palavra)
ultimas_letras = a[3:] #Pega da posição 4 da palvra pra lá
print(ultimas_letras)
b = a.replace('aco' , 'amento') #Para trocar parte da palavra
print(a)
print(b)
c = a.replace('o' , 'a')
print(c)
c.find('s')
e = ' casaco '
print(len(e))
f = e.strip()
print(f)
print(len(f))
n1 = 20
n2 = 15
print('Dividindo {} por {} o resultado é {:.2f}'.format(n1 , n2, n1/n2))









