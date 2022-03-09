#Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

print('='*15)
print('10 TERMOS DE UMA PA')
print('='*15)

start = int(input('Primeiro termo: '))
razao = int(input('RAZAO: '))
decimo = start + (10-1) * razao

for c in range(start, decimo + razao, razao):
    print('{} '.format(c), end='→')
print('acabou')