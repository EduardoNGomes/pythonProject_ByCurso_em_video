#Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
# cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

dt = float(input('Qual sera a distancia que voce pretende viajar? '))
if dt <= 200:
    print('O valor da viagem ficara em R${:.2f},aproveite sua viagem.'.format(dt*0.50))
else:
    print('O valor da viagem ficara em R${:.2f},aproveite sua viagem.'.format(dt*0.45))
