# Exercício de Estruturas de Repeetição
nota = media = soma = 0
for _ in range(1, 6):
    nota = float(input('Digite a nota: '))
    soma += nota
print('A soma de todas elas é', soma)
media = soma / 5
print('A média é', media)
print('----')

# Outra forma de fazer usando o while
nota = soma = 0
numero = 1
while numero <= 5:
    nota = float(input('Digite sua nota: '))
    soma += nota
    numero += 1
print('A média é', soma / 5)


