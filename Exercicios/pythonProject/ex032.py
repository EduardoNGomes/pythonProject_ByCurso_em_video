#Exercício Python 032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from datetime import date

year = int(input('Qual e o ano que voce quer analisar? Coloque 0 para analisar o ano atual. '))
if year == 0:
    year = date.today().year
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('O ano {} e um ano Bissexto'.format(year))
else:
    print('o ano {} NAO e um ano Bissexto'.format(year))

