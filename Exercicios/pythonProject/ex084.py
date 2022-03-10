#Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.


temp = []
geral = []

maior = menor = 0

while True:
    temp.append(str(input('Nome: ')))
    temp.append(int(input('Peso: ')))

    if len(geral) == 0: #Verificando se o Array esta vazio.
        maior = menor = temp[1]   # Como o ARRAY esta vazio o peso e o maior e menor.
    else: 
        if temp[1] > maior: # Se o peso for MAIOR que o esta armazenado, o peso armazenado sera substituido.
            maior = temp[1] 

        if temp[1] < menor: #Se o peso for MENOR que o esta armazenado, o peso armazenado sera substituido.
            menor = temp[1]

    geral.append(temp[:]) #Clonando a lista segundaria(TEMP) para a principal(GERAL)
    temp.clear() # Zerando lista segundaria para nao ter elementos duplicados.

    answer = str(input('Deseja continuar[S/N]? ')).strip()[0] # Saindo do LOOP de acordo com a resposta.
    if answer not in 'Ss':
        if answer in 'Nn':
            break
        else:
            print('Opcao invalida')

print(f'Quantidade de pessoas cadastradas: {len(geral)}') #Exibindo quantidade de elementos existentes na lista.

print(f'O maior peso foi de {maior}KG. Peso de ',end='')
for p in geral:# Analisando todos os elementos da lista(GERAL)
    if p[1] == maior: # Verificando se o peso(p[1]) e igual ao que esta armazenado na varialvel(MAIOR).
        print(f'{p[0]} ',end='')#Listando o nome da pessoa(p[0])

print()


print(f'O menor peso foi de {menor}KG. Peso de ',end='')
for p in geral:
    if p[1] == menor: #Verificando se o peso(p[1]) e igual ao que esta armazenado na varialvel(MENOR).
        print(f'{p[0]} ', end='')#Listando o nome da pessoa(p[0])
    
