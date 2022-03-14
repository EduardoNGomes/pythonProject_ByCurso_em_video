#Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(a,b):
    t = a*b
    print(f'A area de um terreno de {a}x{b} e de {t}m².')


#Programa principal
print('     Controle de terrenos     ')
print('-'*10)

a = float(input('Largura (m): '))
b = float(input('Coprimento (m): '))

area(a, b)