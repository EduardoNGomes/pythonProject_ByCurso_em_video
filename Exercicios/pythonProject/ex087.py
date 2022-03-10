#Exercício Python 087: Aprimore o desafio anterior, mostrando no final: 
#A) A soma de todos os valores pares digitados.
#B) A soma dos valores da terceira coluna.
#C) O maior valor da segunda linha.

matriz = [[0,0,0],[0,0,0],[0,0,0]]
spar = mai = scol =  0

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))

print('-='*30)

for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]}]',end='')
        if matriz[l][c] % 2 == 0: # Testando se o valor armazenado e par
            spar += matriz[l][c]
    print()

print ('-='*30 )
print(f'A soma dos valores pares e : {spar}')

for l in range(0,3):# loop para armazenar e somar todas os elmentos da terceira coluna - matriz[l][2]
    scol += matriz[l][2]
print('A soma dos valores da terceira coluna e {scol}')

for c in range(0,3): #loop para saber qual e o maior elemento da segunda linha - matriz[1][c]
    if c == 0 or matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da segunda linha e {mai}')
