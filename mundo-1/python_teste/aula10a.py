n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('Sua media foi de : {}'.format(m))
#print('parabens' if m >=6 else 'Estude mais')
if m >= 6:
    print('Parabens voce foi aprovado')
else:
    print('Infelizmente voce nao obteve uma media suficiente para prosseguir')
