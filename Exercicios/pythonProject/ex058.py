#Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
#Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

computer = randint(1,10)
print('Acabei de pensar em um numero entr 1 e 10.\nVoce consegue advinhar qual foi?')
user = int(input('Qual e o seu palpite? '))
count = 0

while user != computer:
    count += 1
    if computer < user:
        print('\033[41mVoce errou!Tente um numero menor...\033[m')
        user = int(input('Qual seu palpite? '))
    else:
        print('\033[41mVoce errou!Tente um numero maior...\033[m')
        user = int(input('Qual o seu palpite? '))

print('\033[42mVoce Acertou!\033[m')
print('Para acertar foi necessario {} tentativas'.format(count))
