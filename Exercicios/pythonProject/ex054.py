#Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas. No final,
# mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date

countOld = 0
countYoung = 0
currentYear = date.today().year
for c in range(1, 8):
    age = int(input('Em que ano a {} nasceu? '.format(c)))
    if currentYear - age >= 18:
        countOld += 1
    else:
        countYoung +=1
print('Ao todo tivemos {} pessoas maiores de idade.'.format(countOld))
print('E tambem {} pessoas menores de idade.'.format(countYoung))

