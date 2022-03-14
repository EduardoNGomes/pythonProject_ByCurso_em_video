#Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.


def maior(* num):                                   #Criando a funcao maior passando por parametro para o metodo para receber diversos n

    print('-=-'*15)                                 #APENAS FORMATACAO
    print('Analisando os valores passados...')      #APENAS FORMATACAO
    if len(num) == 0:                               #Verificando se foi passado algum parametro
        print('Nao foi informado nenhum valor')     #Mostrando msg caso o parametro esteja vazio
    else:                                           #Parametro nao esta vazio
        print()                                     #APENAS FORMATACAO
        for n in num:                               #Loop para mostrar cada numero passado por parametro
            print(n,end=' ')                        #Mostrando os numeros
        sorted(num)                                 #Ordenando os numeros do maior para o menor
        print(f'Foram informados {len(num)}\nO maior valor digitado e {max(num)}') #Exibindo qdte de numeros e qual foi o maior
    print('-=-'*15)                                 #APENAS FORMATACAO
    print()                                         #APENAS FORMATACAO


maior(2,9,4,5,7,1)                                  #Chamando a funcao maior passando os numeros por parametros

maior(4,7,0)                                        #Chamando a funcao maior passando os numeros por parametros

maior(1,2)                                          #Chamando a funcao maior passando os numeros por parametros

maior(6)                                            #Chamando a funcao maior passando os numeros por parametros

maior()                                             #Chamando a funcao maior deixando o parametro vazio.

