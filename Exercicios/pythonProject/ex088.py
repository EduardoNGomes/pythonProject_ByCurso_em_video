#Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep

print('='*20)
print('         JOGO DA MEGA-SENA          ')
print('='*20)

n = int(input('Quantos jogos voce quer que eu sorteie? ')) # Armazenado a qtde de jogos que serao feitos
jogos = []
lista = []

c = 1
print(f'SORTEANDO {n} JOGOS')
sleep(1)

while c <= n: # Loop para a quantida de JOGOS que o usuario solicitou
    cont = 0 # variavel de saindo do LOOP WHILE TRUE
    while True:
        num = randint(1,60) # Sorteio de numeros
        if num not in lista:    # Verificando se os numero ja nao estao em lista para nao haver repeticao
            lista.append(num) # Adicionado numero a lista
            cont += 1
        if cont >= 6: # Condicao para saido do LOOP
            break
    lista.sort()#Organizando a lista
    jogos.append(lista[:]) #CLONANDO a LISTA para JOGOS
    lista.clear() # Limpando a lista
    c += 1 #Saido do LOOP while 

for i,l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
