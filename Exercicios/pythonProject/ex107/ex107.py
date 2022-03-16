#Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

import moeda

p = float(input('Digite um preco: '))
t = int(input('Digite a taxa de juros:'))

print(moeda.aumentar(p,t))
print(moeda.diminuir(p,t))
print(moeda.dobro(p))
print(moeda.metade(p))