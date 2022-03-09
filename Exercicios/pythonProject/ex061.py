#Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

print('=-='*20)
print('\033[7mGERADOR DE PA\033[m')
firsTerm = int(input('Primeiro termo: '))
reason = int(input('Razao da PA: '))
term = firsTerm
count = 10

while count >= 1:
    print('{} → '.format(term),end='')
    term += reason
    count -= 1
print('FIM')
