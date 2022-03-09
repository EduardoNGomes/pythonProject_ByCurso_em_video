#Exercício Python 035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou
# não formar um triângulo.
from time import sleep
print('-=-'*15)
print('Analisador de triangulos')
print('-=-'*15)

print('Por favor digite 3 medidas para podermos avaliar se sera ou nao possivel criar um triangulo com as mesmas.')
r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))

print('PROCESSANDO...')
sleep(1)

if r1+r2 > r3 and r1+r3 > r2 and r2+r3 > r1:
    print('E possivel formar um triangulo com estas medidas.')
else:
    print('Infelizmente nao e possivel formar um triangulo com estas medidas.')

print('-=-'*15)
