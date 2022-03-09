#Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
# mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

answer = 's'
count = 0
total = 0

maior = 0
menor = 0


while answer not in 'n':
    number = int(input('Digite um numero: '))
    answer = str(input('Deseja continuar [S/N] ? ')).lower().strip()[0]
    if count == 0:
        maior = number
        menor = maior
    else:
        if number > maior:
            maior = number
        elif number < menor:
            menor = number
    count += 1
    total += number
print('Voce digitou {} numeros e a media foi {}'.format(count, total/count))
print('O maior valor digitado foi {}.\nO menor valor digitado foi {}.'.format(maior, menor))






