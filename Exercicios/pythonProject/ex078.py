#Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o #menor valor digitado e as suas respectivas posições na lista.

valores = []

for c in range(0,4):#Entrada de valores na lista
    valores.append((int(input(f'Digite um valor para a posicao {c}: '))))
print(f'Voce digitou os valores: {valores}')
print(f'O maior valor digitado foi \033[7m{max(valores)}\033[m nas posicoes ',end='')# Mostrando maior valor
for c,v in enumerate(valores):# Verificando os indices do maior valor
    if v == max(valores):
        print(c, end=' ')
print(f'\nO menor valor digitado foi \033[7m{min(valores)}\033[m nas posicoes ',end='')# Mostrando menor valor
for c, v in enumerate(valores):# Verificando o indice do menor valor
    if v == min(valores):
        print(c,end=' ')