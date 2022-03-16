#Exercício Python 108: Adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.
import moeda

p = float(input('Digite um preco: '))
t = int(input('Digite a taxa de juros:'))

print(f'Aumentando {t}% temos,{moeda.moeda(moeda.aumentar(p,t))}')
print(f'Diminuindo {t}% temos,{moeda.moeda(moeda.diminuir(p,t))}')
print(f'O dobro de {moeda.moeda(p)} e {moeda.moeda(moeda.dobro(p))}')
print(f'A metade de {moeda.moeda(p)} e {moeda.moeda(moeda.metade(p))}')