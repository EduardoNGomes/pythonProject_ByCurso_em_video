#Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador.
#O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
print('=-='*20)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-='*20)

count = 0
while True:
    player = int(input('Escolha um numero: '))
    computer = randint(1, 10)
    choice = str(input('Par ou Impar? [P/I] ')).upper().strip()[0]
    if choice == 'P' and (player + computer) % 2 == 0:
        print(f'Voce escolheu {player} e o computador escolheu {computer}')
        print('Jogador \033[42mVENCEU\033[m', end='')
        print('Deu par 'if ((player + computer) % 2 == 0) else 'Deu impar')
        count += 1
    elif choice == 'I' and (player + computer) % 2 == 1:
        print(f'Voce escolheu {player} e o computador escolheu {computer}')
        print('Jogador \033[42mVENCEU\033[m')
        count += 1
    elif choice not in 'PpIi':
        print('\033[41mCOMANDO INVALIDO\033[m')
    else:
        print(f'Voce escolheu {player} e o computador escolheu {computer}')
        print('Jogador \033[41mPERDEU\033[m')
        break
    print('Vamos jogar novamente...')
print('=-='*20)
print(f'\033[41mGAME OVE\033[m\nJogador venceu {count} vezes')
