#Exercício Python 055: Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

bigger = 0
short = 0
for c in range(1,6):
    weight = float(input('Peso da {} pessoa: '.format(c)))
    if c == 1:
        bigger = weight
        short = weight
    else:
        if weight > bigger:
            bigger = weight
        if weight < short:
            short = weight
print('Mais pesado {}'.format(bigger))
print('Mais leve {}'.format(short))


