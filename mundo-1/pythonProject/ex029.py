#Exercício Python 029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
#mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

speed = float(input('Qual e foi a velocidade alcancada pelo veiculo? '))
if speed > 80:
    print('Voce ultrapassou o limite permitido de 80km/h e infelizmente sera multado em R$ 7.00 para cada km ultrapassado.')
    print('A multa sera no valor de R${:.2f} .'.format((speed-80)*7))
else:
    print('Tenha um bom dia e dirija com seguranca')
