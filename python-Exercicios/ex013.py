lista = []
try:
    lista.append(float(input('Digite o valor 1: ')))
    lista.append(float(input('Digite o valor 2: ')))
    divisao = lista[0] / lista[1]
except ValueError:
    print('Erro. Valor inválido!')
except ZeroDivisionError:
    print('Erro. Divisão por zero! ')
except IndexError:
    print('Erro. Índice inválido!')
except KeyboardInterrupt:
    print('Erro. Interrompeu a execução!')
else:
    print(f'O resultado da divisão dos dois valores é {divisao}')