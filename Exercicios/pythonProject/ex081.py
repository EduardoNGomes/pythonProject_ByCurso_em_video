#Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
#A) Quantos números foram digitados.
#B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista.

numbers = []

while True:
    numbers.append(int(input('Digite um valor: ')))# Solicitando elementos e colocando na lista.
    
    answer = str(input('Deseja continuar[S/N]? ')).strip()[0]# Pergunta para sair do loop
    if answer not in 'Ss':
        if answer in 'Nn':
            break
        else:
            print('\033[41mOPCAO INVALIDA\033[m')
print(f'A quantidade de numeros digitados foi de {len(numbers)}')# Quantidade de elementos dentro da lista
print(f'Os numeros digitados em ordem decrescente: {sorted(numbers,reverse=True)}') # Exibindo a lista de forma decrescente
if 5  in numbers:# Verificando se dentro da lista ha o numero 5.
    print('O numero 5 faz sim parte da lista.')
else:
    print('O numero 5 nao faz parte da lista.') 