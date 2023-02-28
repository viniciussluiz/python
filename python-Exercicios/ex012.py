import leitura as lt
texto = lt.ler_string('Digite seu nome: ')
print('Seu nome é', texto)
carro = lt.ler_string('Digite qual é o seu carro: ')
print('Seu carro é', carro)
numero = lt.ler_float('Digite sua idade: ')
print('Você tem', numero, 'anos')
numero1 = lt.ler_float('Digite um valor: ')
print('Seu valor é', numero1)
numero2 = lt.ler_float('Digite outro valor:')
print('Seu segundo valor é', numero2)
soma = numero1 + numero2
print('A soma dos dois valores é', soma)