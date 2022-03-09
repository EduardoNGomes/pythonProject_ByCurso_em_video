#Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
#No final, mostre uma listagem de preços, organizando os dados em forma tabular.

list = ('Casa' , 500000,
        'Carro', 30000,
        'Aviao', 800000,
        'Jato', 506000,
        'Jet Ski', 100000)
print('-'*30)
print('LISTAGEM DE PRECO')
print('-'*30)

for item in range(0, len(list)):
    if item % 2 == 0:
        print(f'{list[item]:.<30}',end='')
    else:
        print(f'R$ {list[item]:>5.2f}')
