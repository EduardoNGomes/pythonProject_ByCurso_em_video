#Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.


value = tuple(int(input('Digite um numero: ')) for c in range(1,5))
print(f'Voce digitou os valores {value}')
print(f'O numero nove foi digitado {value.count(9)} vez(es)')
if 3 in value:
    print(f'O numero 3 foi digitado na posicao {value.index(3)+1}')
else:
    print('O valor 3 nao foi digitado em nenhuma posicao')
print('Os valorers pares digitados foi:', end='')
for n in value:
    if n % 2==0:
        print(n,end=' ')





    