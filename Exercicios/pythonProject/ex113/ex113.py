#Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
from func import leiaInt, leiaFloat

n = leiaInt('Digite um numero: ')   
n2 = leiaFloat('Digite um valor real:  ')          
print(f'Voce acabou de digitar o numero inteiro: {n}') 
print(f'Voce acabou de digitar o numero real: {n2}')
