#Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato

from time import sleep

total = count = cheaper = 0
nameCheaper = ''


while True:
    nameProduct = str(input('Qual o nome do produto? '))
    cust = float(input('Qual o valor do produto? R$ '))
    if nameCheaper == '':
        nameCheaper = nameProduct
        cheaper = cust
    total += cust
    if cust > 1000:
        count += 1
    if cust < cheaper:
        nameCheaper = nameProduct
    answer = str(input('Deseja continuar[S/N]? ')).strip()[0]
    if answer not in 'Ss':
        if answer in 'Nn':
            print('Finalizando')
            sleep(.5)
            break
        else:
            print('Opcao Invalida')

print(f'''
    O valor total gasto nas compras foi de \033[42m{total:.2f}\033[m reais.
    Existem \033[42m{count}\033[mprodutos que custam mais de 1000 reais.
    O nome do produto mais barato e\033[42m{nameCheaper}\033[m.
    
    
''')