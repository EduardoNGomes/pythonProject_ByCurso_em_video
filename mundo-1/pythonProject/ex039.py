#Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
#se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import datetime
age = int(input('Qual seu ano de nascimento? '))
dateArmy = datetime.now().year - age
if dateArmy == 17:
    print('No ano de {} voce esta com {} anos.\033[0;30;42m Voce precisa se alistar esta ano\033[m'.format(datetime.now().year, dateArmy))
elif dateArmy >= 18:
    print('No ano de {} voce esta com {} anos.\033[0;30;41m Voce ja passou da sua data de se alistar\033[m'.format(datetime.now().year, dateArmy))
else:
    print('No ano de {} voce esta com {} anos.\033[0;30;43m Voce ainda e muito jovem para se alistar.\033[m'.format(datetime.now().year, dateArmy))
