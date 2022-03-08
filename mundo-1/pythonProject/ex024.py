#Exercício Python 024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

city = str(input('Qual a cidade que voce nasceu? ')).strip()
print(city[:5].lower() == 'santo')
