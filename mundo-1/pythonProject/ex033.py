#Exercício Python 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = float(input('Digite o primeiro numero: '))
n2 = float(input('Digite o segundo numero: '))
n3 = float(input('Digite o terceiro numero: '))

#Verificando menor numero
short = n1
if n2 < n1 and n2 < n3:
    short = n2
if n3 < n1 and n3 < n2:
    short = n3
print('O menor numero e {}.'.format(short))

#verificando maior numero
big = n2
if n1 > n2 and n1 > n3:
    big = n1
if n3 > n2 and n3 > n1:
    big = n3
print('O maior numero e {} '.format(big))
