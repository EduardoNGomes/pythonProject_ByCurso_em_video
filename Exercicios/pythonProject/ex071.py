# Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.


from tkinter.tix import Tree


print('='*30)
print('         BEM VINDO        ')
print('='*30)
value = int(input('Qual o valor a ser sacado? R$'))
total = value
ced = 50
totced = 0

while True:
    if total >= ced:
        total -= ced
        totced +=1
    else:
        if totced > 0:
            print(f'Total de {totced} cedulas  de R${ced}')
        if ced == 50:
            ced = 20
        if ced == 20:
            ced = 10
        if ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('='*30)
print('Volte sempre')