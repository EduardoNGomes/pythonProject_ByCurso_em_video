#Sem importar modulos
'''
c1 = float(input('Qual o comprimento do cateto oposto? '))
c2 = float(input('Qual o comprimento do cateto adjacente?'))
soma = c1**2 + c2**2
hip = float(soma**0.5)
print(hip)
'''

from math import hypot
co = float(input('Qual o comprimento do cateto oposto? '))
ca = float(input('Qual o comprimento do cateto adjacente? '))
hip = hypot(co, ca)
print('A hipotenusa e {:.2f}'.format(hip))
