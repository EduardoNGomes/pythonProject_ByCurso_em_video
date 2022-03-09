#Exercício Python 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

sex = str(input('Digite o sexo [M/F]: ')).strip()[0]
while sex not in 'MmFf':
    print('\033[30;41mSEXO INVALIDO\033[m')
    sex = str(input('Digite novamente o sexo [M/F]: ')).upper().strip()[0]
print('\033[42mCADASTRO REALIZADO!\033[m')
