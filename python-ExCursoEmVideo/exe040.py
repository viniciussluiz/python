sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Digite novamente: ')).strip().upper()[0]
print('Seu sexo é {}'.format(sexo))