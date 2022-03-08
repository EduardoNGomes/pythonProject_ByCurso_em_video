#Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
#- à vista dinheiro/cheque: 10% de desconto
#- à vista no cartão: 5% de desconto
#- em até 2x no cartão: preço formal
#- 3x ou mais no cartão: 20% de juros

value = float(input('Qual o valor final das compras?'))
pay = int(input('FORMAS DE PAGAMENTO:\n1 - A vista/Cheque : 10% Desconto\n2 - A vista no cartao : 5% Desconto\n3 - Parcelado em ate 2x : Sem Desconto\n4 - Parcelado em mais de 3x : 20% Juros\nQual e a opcao? '))

if pay == 1:
    des = value/100*10
    print('Voce recebera um desconto de 10% nas suas compras')
    print('Ao inves de pagar {}, Voce pagara {}'.format(value, value-des))
elif pay == 2:
    des = value/100*5
    print('''Voce recebera um desconto de 5% nas suas compras,
    ao inves de pagar {}, voce pagara {}'''.format(value, value-des))
elif pay == 3:
    print('Devido a esta forma de pagamento nao sera possivel lhe dar desconto sobre suas compras')
else:
    juros = value/100*20
    print('Devido a esta forma de pagamento voce tera que para um juros de {}, logo suas compras no valor de {}, sairao por {}'.format(juros, value, value+juros))


