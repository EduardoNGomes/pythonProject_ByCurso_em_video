#Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

#numeros = [[],[],[],[],[],[],[],[],[]]

#for c in range(0,9):
#    n = int(input('Valores: '))
#    numeros[c].append(n)
#
#for c in range(0,3):
#    print(numeros[c], end=' ')
#print()
#for c in range(3,6):
#    print(numeros[c], end=' ')
#print()
#for c in range(6,9):
#    print(numeros[c], end=' ')


#           CORRECAO DO PROFESSOR

matriz = [[0,0,0],[0,0,0],[0,0,0]]

for l in range(0,3): # Loop para armazenar as linhas
    for c in range(0,3):# Loop para armazenar as colunas
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))

print('-='*30)

for l in range(0,3): # loop para organizar as linhas
    for c in range(0,3): # loop para organizar as colunas
        print(f'[{matriz[l][c]}]',end='')
    print()