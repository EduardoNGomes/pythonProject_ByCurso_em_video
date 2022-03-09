#Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.

countAge = countM = countF = 0

while True:
    name = str(input('Digite o nome: '))
    age = int(input('Digite a idade: '))
    sex = str(input('Digite seu sexo[M/F]: ')).strip()[0]
    ask = str(input('Deseja continuar[S/N]? ')).strip()[0]
    if age > 18:
        countAge += 1
    if sex in 'Mm':
        countM +=1
    if sex in 'Ff' and age <20:
        countF +=1
    if ask not in 'Ss':
        if ask in 'Nn':
            break
        else:
            print('Opcao invalida')



print(f'''
    A quantidade de pessoas cadrastradas acima de 18 anos foi\033[7m {countAge} \033[m
    A quantidade de Homens cadastrados foi de\033[42m {countM} \033[m
    A quantidade de mulhers cadastradas abaixo de 20 anos foi de\033[44m {countF} \033[m

''')

