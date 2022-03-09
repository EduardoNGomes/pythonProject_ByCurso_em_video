#Exercício Python 063: Escreva um programa que leia um número N inteiro qualquer
#e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.

print('=='*15)
print('Sequencia de FIBONACCI')
print('=='*15)

choice = int(input('Quantos termos voce quer mostrar? '))
t1 = 0
t2 = 1
print('--'*30)
print('{} → {}'.format(t1, t2), end='')
count = 3

while count <= choice:
    t3 = t1 + t2
    print(' → {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    count += 1
print('\nFim')



