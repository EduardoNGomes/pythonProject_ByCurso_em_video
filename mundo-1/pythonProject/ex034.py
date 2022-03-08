#Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

money = float(input('Qual o valor do seu salario atualmente? R$ '))
print('O valor do seu salario e de {:.2f}'.format(money))
if money > 1250:
    print('Voce recebera um aumento de 10%.\nSeu salario sera de R${:.2f}'.format(money+(money/100)*10))
else:
    print('Voce recebera um aumento de 15%.\nSeu salario sera de R${:.2f}'.format(money+(money/100)*15))
