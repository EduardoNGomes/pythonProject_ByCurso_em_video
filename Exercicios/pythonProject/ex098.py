#Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:

#a) de 1 até 10, de 1 em 1
#b) de 10 até 0, de 2 em 2
#c) uma contagem personalizada

from time import sleep

def contador(a, b, c):                                  #Criando funcao 

    if c < 0:                                           #Verificando se o valor de c sera negativo
        c *= -1                                         #Multiplicando o valor negativo por -1 para que le fique positivo
    if c == 0:                                          #Verificando se o valor de c e igual a 0
        c = 1                                           #Adicionando o valor 1 a c para que a funcao possa ocorer
    
    print('-='*20)                                      #Apenas formatacao
    print(f'Contagem de {a} ate {b} de {c} em {c}')     #Mostrando os parametros 

    if a < b:                                           #Verificando se A e menor que B para fazer uma contagem crescente
        cont = a
        while cont <= b:
            print(cont, end=' ', flush=True)
            sleep(.4)
            cont += c 
    else:                                               #Caso nao seja ira ser feita uma contagem decrescente
        cont = a
        while cont >= b:
            print(cont,end=' ',flush=True)
            sleep(.4)
            cont -= c
    print()
    print('=-'*20)                                      #Apenas formatacao
    print()
        


contador(1,10,1)                                        #Chamando funcao contador passando os parametros

contador(10,0,2)                                        #Chamando funcao contador passando os parametros

print('Agora e sua vez de personalizar a contagem')     #APENAS FORMATACAO
i = int(input('Inicio: '))                              #Guardando um valor na variavel
f = int(input('Fim: '))                                 #Guardando um valor na variavel
p = int(input('Passo: '))                               #Guardando um valor na variavel

contador(i,f,p)                                         #Chamando a funcao contador com as variaveis como parametro