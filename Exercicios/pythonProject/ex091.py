#Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter

#Criando dicionario com 4 keys e randomizando 1 value para cada key
nu = {'Jogador1': randint(1,6),
      'Jogador2': randint(1,6),
       'Jogador3': randint(1,6), 
       'Jogador4 ': randint(1,6)}
ranking = list()    #Criacao de lista para organizar os elementos de nu

print('Valores sorteados: ')

for k,v in nu.items():      #Exibindo cada key(JOGADORES) e seus values(numeros sorteados)
    print(f'{k} tirou {v}')
    sleep(.5)

ranking = sorted(nu.items(),key=itemgetter(1),reverse=True)     # Adicionando os elemento de (NU) a lista(ranking) para organizar(sorted()) os numeros sorteados(itemgetter(1)) de maneira decrescente(reverse=True)

print('='*20)
print('== RANKING DOS JOGADORES ==')

for i,v in enumerate(ranking):      #Analisando a Lista(ranking)
    print(f'{i+1} lugar: {v[0]} com {v[1]}.')   #i = posicao atual  | v[0] = jogador | v[1] = numero sorteado
    sleep(.5)
