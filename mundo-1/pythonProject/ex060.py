#Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.
#Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

#USANDO METADO FATCTORIAL
from math import factorial
#print('=-='*20)
#print('NUMERO FATORIAL')
#print('=-='*20)
#number = int(input('Digite um numero: '))
#f = factorial(number)
#print('O fatorial de {} e {}'.format(number, f))

#USANDO WHILE

print('=-='*20)
print('NUMERO FATORIAL')
print('=-='*20)
number = int(input('Digite um numero: '))
count = number
f = 1
print('Calculando {}!= '.format(number), end='')
while count > 0:
    print('{} '.format(count), end='')
    print(' x ' if count > 1 else ' = ', end='')
    f *= count
    count -= 1
print('{}'.format(f))






