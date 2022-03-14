#Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def calcArea(a,b):                                          #Criacao da funcao area
    t = a*b                                                 #Realizando o calcula da area   
    print(f'A area de um terreno de {a}x{b} e de {t}m².')   #Mostrando parametros passados com o resultado 


#Programa principal
print('     Controle de terrenos     ')                     #APENAS FORMATACAO
print('-'*10)                                               #APENAS FORMATACAO

a = float(input('Largura (m): '))                           #Armazenando um parametro
b = float(input('Coprimento (m): '))                        #Armazenando um parametro

calcArea(a, b)                                              #Chamando a funcao calcArea passando os parametros