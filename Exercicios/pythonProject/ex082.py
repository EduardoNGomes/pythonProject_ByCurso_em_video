#Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.




numbers = []
numberP = []
numberI = []
while True:
    n = int(input('Digite um numero: '))# Armazendo numero em variavel
    if n % 2 == 0: # Verificando se a variavel e PAR e armazendo ela no array de numeros e de numeros PARES
        numbers.append(n)
        numberP.append(n)
    else: # Se ele nao for PAR sera IMPAR e deve ser armazenada no array de numeros e de numeros IMPARES
        numberI.append(n)
        numbers.append(n)

    answer = str(input('Deseja continuar[S/N]? ')).split()[0] # Pergunta para interromper o loop
    if answer not in 'Ss':
        if answer in 'Nn':
            break
        else:
            print('\033[41mOPCAO INVALIDA\033[m')

#Exibicao dos resultados
print(f'A lista em geral possui os seguintes valores: {sorted(numbers)}')
print(f'A lista de valores PARES possui os seguintes valores: {sorted(numberP)}')
print(f'A lista de valores IMPARES possui os seguintes valores: {sorted(numberI)}')
    