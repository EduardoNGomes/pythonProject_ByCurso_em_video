#Exercício Python 066: Crie um programa que leia números inteiros pelo teclado.
#O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
#No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).


count = soma = 0

while True:
    number = int(input('Digite um numero (999 para parar): '))
    if number == 999:
        break
    soma += number
    count += 1
print(f'A quantidade de numeros digitados foi {count} e a soma de todos os valores e de {soma}.')