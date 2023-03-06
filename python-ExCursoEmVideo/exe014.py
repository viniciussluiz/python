nome = str(input('Digite seu nome: ')).strip()
print('''Analisando seu nome...
Seu nome em maiúsculas é {}
Seu nome em minúsculas é {}
Seu nome tem {} letras
'''.format(nome.upper(), nome.lower(), len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras.'.format(separa[0], len(separa[0])))
