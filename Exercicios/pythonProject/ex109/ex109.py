#Exercício Python 109: Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
import moeda

p = float(input('Digite um preco: '))
t = int(input('Digite a taxa de juros:'))

print(f'Aumentando {t}% temos,{moeda.aumentar(p,t,True)}')
print(f'Diminuindo {t}% temos,{moeda.diminuir(p,t,True)}')
print(f'O dobro de {moeda.moeda(p)} e {moeda.dobro(p,True)}')
print(f'A metade de {moeda.moeda(p)} e {moeda.metade(p,True)}')