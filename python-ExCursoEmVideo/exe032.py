from datetime import date
atual = date.today().year
ano = int(input('Qual ano você nasceu? '))
idade = atual - ano
if idade <  18:
    print('Você tem {} anos e ainda vai se alistar no exército. Em {} ano(s) você deverá se alistar'.format(idade, 18 - idade))
elif idade == 18:
    print('Está na idade de se alistar no exército.')
else:
    print('Você tem {} ano(s). Já passou do tempo de se alistar. Há {} ano(s) você deveria ter se alistado'.format(idade, idade - 18))
