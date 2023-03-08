salario = float(input('Qual o valor do seu salário, em R$? '))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Seu salário era R${:.2f}, mas com o aumento será R${:.2f}.'.format(salario, novo))
