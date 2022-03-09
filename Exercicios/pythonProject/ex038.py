#Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#- O primeiro valor é maior
#- O segundo valor é maior
#- Não existe valor maior, os dois são iguais

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))

if n1 > n2:
    print('\033[0;34;40mO primeiro valor e maior.\033[m')
elif n2 > n1:
    print('\033[0;32;40mO segundo valor e maior.\033[m')
else:
    print('\033[0;37;40mNao existe valor maior, os dois sao iguais.\033[m')