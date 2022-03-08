#Exercício Python 027: Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.

name = str(input('Digite seu nome completo: '))
fname = name.split()
print('Prazer em te conhecer! Seu primeiro nome e {}.'.format(fname[0]))
print('Seu ultimo nome e {}'.format(fname[len(fname)-1]))
