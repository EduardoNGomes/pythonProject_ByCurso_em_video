#Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
#- O nome com todas as letras maiúsculas e minúsculas.
#- Quantas letras ao todo (sem considerar espaços).
#- Quantas letras tem o primeiro nome.


name = str(input('Digite seu nome completo ')).strip()
print('Seu nome com todas as letras maiusculas e {}'.format(name.upper()))
print('Seu nome com todas as letras minusculas e {}'.format(name.lower()))
print('Seu nome tem ao todo {} letras'.format(len(name) - name.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(name.find(' ')))
separa = name.split()
print('Seu primeiro nome e {} e tem {} letras'.format(separa[0], len(separa[0])))