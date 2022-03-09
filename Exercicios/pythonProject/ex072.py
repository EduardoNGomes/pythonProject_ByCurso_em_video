#Exercício Python 072: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

numbers = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    value = int(input('Digite um numero entre 0 e 20: '))
    if value <= 0 or value >= 20:
        print('\033[41mValor Invalido\033[m')
    else:
        print(f'Voce digitou {numbers[value]}')
        answer = str(input('Deseja continuar[S/N]? ')).strip()[0]
        if answer not in 'Ss':
            if answer in 'Nn':
                break
            else:
                print('\033[41mOpcao Invalida\033[m')
