#Estrutura aninhada - elif-

name = str(input('Qual e o seu nome? '))
if name == 'Eduardo':
    print('Parabens pelo belo nome')
elif name == 'Joao' or name == 'Maria' or name == 'Jose':
    print('Seu nome e bem popular no brasil')
else:
    print('Seu nome e comum')
print('Tenha um bom dia, {}!'.format(name))
