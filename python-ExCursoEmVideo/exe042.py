n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa ''')
    opção = int(input('>>>> Qual é a sua opção? '))
    if opção == 1:
        print('A soma dos dois números é {}'.format(n1 + n2))
    elif opção == 2:
        print('A multiplicação dos números é {}'.format(n1 * n2))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre o número {} e o número {}, o maior é {}.'.format(n1, n2, maior))
    elif opção == 4:
        print('Digite os números novamente')
        n1 = int(input('Primeiro número: '))
        n2 = int(input('Segundo número: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida!')
    print('=-=' * 10)
print('Fim do programa. Volte sempre!')
