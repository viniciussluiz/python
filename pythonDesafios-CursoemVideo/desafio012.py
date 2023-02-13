sal = float(input('Qual é o valor do seu salário(em reais)? '))
aum = (sal / 100)*15
ns = sal + aum
print('A partir de hoje com o aumento de 15% no seu salário de R${:.2f}, ele aumetará em R${:.2f} e você passará a receber R${:.2f}'.format(sal, aum, ns))