with open('pythonEstudos/frase.txt') as tex:
    for linha in tex:
        print(linha)

with open('texto2.txt', 'w') as texto:
    texto.write('Olá a todos')

