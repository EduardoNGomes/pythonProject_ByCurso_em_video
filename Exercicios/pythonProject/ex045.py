#Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.
from time import sleep
from random import randint

print(' JO KEN PO ')
print('''Suas opcoes:
    [ 0 ] PEDRA
    [ 1 ] PAPEL
    [ 2 ] TESOURA
''')
optionPlayer = int(input('Qual e a sua jogada? '))
optionPc = randint(0,2)

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)

if optionPlayer == 0 and optionPc == 1:
    print('''
    Voce escolheu PEDRA
    O Computador escolheu PAPEL
    Voce PERDEU  
    ''')
elif optionPlayer == 1 and optionPc == 2:
    print('''
    Voce escolheu PAPEL
    O computador escolhe TESOURA
    Voce PERDEU
    ''')
elif optionPlayer == 2 and optionPc == 0:
    print('''
    Voce escolheu TESOURA
    O computador escolheu PEDRA
    Voce PERDEU
    ''')
elif optionPc == 0 and optionPlayer == 1:
    print('''
    Voce escolheu PEDRA
    O Computador escolheu PAPEL
    Voce VENCEU 
    ''')
elif optionPc == 1 and optionPlayer == 2:
    print('''
    Voce escolheu PAPEL
    O computador escolhe TESOURA
    Voce VENCEU
    ''')
elif optionPc == 2 and optionPlayer == 0:
    print('''
    Voce escolheu TESOURA
    O computador escolheu PEDRA
    Voce VENCEU
    ''')
elif optionPc == optionPlayer :
    print('EMPATE')
else:
    print('ESCOLHA INVALIDA')





