from util import moeda
from util import dados


p = dados.leiaDinheiro('Digite o preco: ')
t = int(input('Digite a taxa de juros: '))

print(f'Aumentando {t}% temos,{moeda.aumentar(p,t,True)}')
print(f'Diminuindo {t}% temos,{moeda.diminuir(p,t,True)}')
print(f'O dobro de {moeda.moeda(p)} e {moeda.dobro(p,True)}')
print(f'A metade de {moeda.moeda(p)} e {moeda.metade(p,True)}')

