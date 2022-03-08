#Exercício Python 026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
#em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

phrase = str(input('Digite um frase')).lower().strip()
print('A letra  "A" aparece {} vezes.'.format((phrase.count('a'))))
print('A letra "A" aparece pela primeira vez na posicao {}.'.format(phrase.find('a')+1))
print('A letra "A" aparece pela ultima vez na posicao {}'.format(phrase.rfind('a')+1 - phrase.count(' ')))


