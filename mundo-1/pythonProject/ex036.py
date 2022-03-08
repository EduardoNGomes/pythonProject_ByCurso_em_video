#Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

value = float(input('Qual o valor da residencia que deseja adquirir? R$ '))
money = float(input('Qual o valor do seu salario? R$ '))
year = int(input('Em quantos anos o senhor deseja finalizar o pagamento? '))


part =(value/(year*12))
print('O valor da prestacao sera de R$ {:.2f}'.format(part))

if (money/100)*30 < value/(year*12):
    print('Infelizmente voce nao pode comprar esta casa com seu salario atual\n\033[0;30;41mEMPRESTIMO NEGADO!\033[m')
else:
    print('\033[0;30;42mParabens seu emprestimo foi aprovado\033[m')
