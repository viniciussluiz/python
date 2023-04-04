casa = float(input('Qual o valor da casa? '))
salário = float(input('Qual é o seu salário? '))
anos = int(input('Em quantos anos você vai pagar? '))
prestação = casa / (anos * 12)
mínimo = salário * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}'.format(casa, anos, prestação))
if prestação <= mínimo:
    print('Empréstimo aprovado!')
else:
    print('Empréstimo negado!')
