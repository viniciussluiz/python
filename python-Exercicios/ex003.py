idade = int(input('Digite sua idade: '))
if idade >= 0 and idade <= 12:
    print('Você é uma criança')
elif idade >= 13 and idade < 18:
    print('Você é adolescente')
elif idade >= 18 and idade < 60:
    print('Você é adulto')
elif idade >= 60:
    print('Você é idoso')
else:
    print('Idade inválida')