#Listas Parte 2 -Lista Composta
from traceback import print_tb


galera = []
dado = []

totmai = totmen = 0

for c in range(0,3):
    dado.append(str(input('Nome: '))) # Adicionando elementos no array  
    dado.append(int(int('Idade: ')))    # Adicionando elementos no array
    galera.append(dado[:])  #Clonando o Array DADO para o array GALERA
    dado.clear()    #Zerando o Array dado

for p in galera: #Pesquisando dentro o Array GALERA
    if p[1] >= 21: # Verificando a idade(indice[1]) e maior que 21 anos
        print(f'{p[0]} e maior de idade') # Respondendo com o nome(indice[0])
        totmai += 1
    else:
        print(f'{p[0]} e menor de idade.')
        totmen += 1
print(f'Temos {totmai} maiors e {totmen} menores de idade')