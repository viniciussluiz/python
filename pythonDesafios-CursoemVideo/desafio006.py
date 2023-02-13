nome = input('Qual é o nome do aluno? ')
ano = input('Em qual ano ele está? ')
n1 = int(input('Qual a nota dele na primeira prova? '))
n2 = int(input('Qual a nota na segunda prova? '))
s = n1 + n2
m = s / 2
print('A média do aluno {}, do {} foi {}'.format(nome, ano, m))