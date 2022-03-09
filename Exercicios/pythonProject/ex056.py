#Exercício Python 056: Desenvolva um programa que
# leia o nome, idade e sexo de 4 pessoas.
#No final do programa, mostre: a média de idade do grupo,
#qual é o nome do homem mais velho
#e quantas mulheres têm menos de 20 anos.

totalAge = 0
count = 0
old = 0
nameOld = ''
for c in range(1, 5):
    print('----- {} PESSOA -----'.format(c))
    name = str(input('Nome: '))
    age = int(input('Idade: '))
    sex = str(input('Sexo [M/F]: ')).upper()

    if sex == 'M':
        if c == 1:
            old = age
        else:
            if age > old:
                old = age
                nameOld = name
    if sex == 'F' and age < 20:
        count += 1

    totalAge += age

print('A media de idade do grupo e de {:.1f}'.format(totalAge/4))
print('O homen mais velho tem {} anos e se chama {}.'.format(old, nameOld))
print('Ao todo sao {} mulheres com menos de 20 anos'.format(count))

