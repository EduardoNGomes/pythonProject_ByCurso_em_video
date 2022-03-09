#Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.



words = ('Casa', 'Carro', 'Roupa','Brinquedo', 'Armario', 'Luvas', 'Prato', 'Faca', 'Garfo', 'Comida', 'Bomba')

for item in words:#Mostrar a lista item por item
    print(f'Na palavra {item} temos ',end='')
    for letras in item:#Mostra as vogais, analisando letra por letra
        if letras in 'aeiouAEIOU':
            print(letras,end='')
    print()