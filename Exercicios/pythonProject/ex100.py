#Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.


from random import randint                                              #Importando biblioteca para sortear numeros aleatorio


def sorteia(lista):                                                     #Criando Funcao sorteia passando lsita por parametro
    
    for i in range(0,5):                                                #Loop de repeticao de 5 vezes
        lista.append(randint(1,10))                                     #Sorteando e adicionando numeros aleatorios a lista
    
    print('Sorteando 5 valores da lista:', end=' ')                     #APENAS FORMATACAO
    for n in lista:                                                     #Loop para mostrar numeros da lista
        print(n, end=' ')                                               #Exibindo cada numero da lista
    print('PRONTO!')                                                    #Apenas formatacao

def soma(lista):                                                        #Criando funcao soma passando lista como parametro
    value = 0                                                           #Variavel para somar os valores
    for n in lista:                                                     #Loop para percorrer cada numero na lista
        if n % 2 == 0:                                                  #Verificando se o numero atual e divisivel por 2
            value += n                                                  #Realizando a soma dos valores divisiveis por dois 
    print(f'Somando os valores pares de  {lista} temos : {value}')      #Exibindo os valores da lista e a soma dos valores pares


num = list()                                                            #Criando de lista vazia

sorteia(num)                                                            #Chamando funcao sorteia passando (num) como parametro
soma(num)                                                               #Chamando funcao soma passando (num) como parametro