# Exercício Python 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
from time import sleep

npc = randint(1, 5)
print('-='*20)
print('Vou pensa em um numero entre 0 e 5. Tente advinhar...')
print('-='*20)
nuser = int(input('Em que numero eu pensei? '))
print('PROCESSANDO...')
sleep(2)
print('O numero pensado por mim foi {}.'.format(npc))
if npc == nuser:
    print('Parabens, voce escolheu {} e acertou!'.format(nuser))
else:
    print('Nao foi desta vez, voce escolher {} e errou!'.format(nuser))
