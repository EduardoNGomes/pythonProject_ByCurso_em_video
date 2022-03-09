#Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem #de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint

lista = (randint(1,100), randint(1,100), randint(1,100), randint(1,100), randint(1,100))



print(f'Os numeros gerados foram {lista}')
print(f'O maior numero gerado foi {sorted(lista)[-1]}')
print(f'O menor numero gerado foi {sorted(lista)[0]}')
