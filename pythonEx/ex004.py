m1 = float(input('Qual foi sua primeira nota? '))
m2 = float(input('Qual foi sua segunda nota? '))
m3 = float(input('Qual foi sua terceira nota? '))
media = (m1 + m2 + m3) / 3
print('Sua nota foi {:.2f}.'.format(media))
if media >= 0.0 and media <= 4.0:
    print('Você está reprovado!')
elif media >= 4.1 and media <= 6.0:
    exame = float(input('Você pegou exame. Qual sua nota no exame? '))
    if exame >= 6.0:
        print('Aprovado no exame.')
    else:
        print('Reprovado no exame.')
else:
    print('Você está aprovado.')