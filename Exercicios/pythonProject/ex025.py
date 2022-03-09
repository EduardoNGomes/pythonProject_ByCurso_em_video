#Exercício Python 025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

name = str(input('Digite seu nome completo'))
print('Seu nome possui SILVA? {}'.format('silva' in name.lower()))
