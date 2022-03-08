#Exercício Python 064: Crie um programa que leia vários números inteiros pelo teclado.
#O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
#No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

#number = 0
#count = 0
#total = 0
#while number != 999:
#    number = int(input('Digite um numero [999 para parar]: '))
#    total += number
#    count += 1
#print('Voce digitou {} numeros e a soma entre eles foi {}'.format(count-1, total-999))

#Correcao:
count = 0
total = 0
number = int(input('Digite um numero [999 para parar]: '))
while number != 999:
    total += number
    count += 1
    number = int(input('Digite um numero [999 para parar]: '))
print('Voce digitou {} numeros e a soma entre eles foi {}'.format(count, total))


