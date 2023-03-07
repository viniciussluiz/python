frase = str(input('Digite uma frease: ')).upper().strip()
print('A letra A aparece {} vezes na frase'.format(frase.count('A')))
print('A primeira letra A apareceu na posicão {} da frase'.format(frase.find('A')+1))
print('A última letra A apareceu na posição {} da frase'.format(frase.rfind('A')+1))