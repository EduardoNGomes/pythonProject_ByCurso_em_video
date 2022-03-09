#Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento
# de um atleta e mostre sua categoria, de acordo com a idade:
#- Até 9 anos: MIRIM
#- Até 14 anos: INFANTIL
#- Até 19 anos: JÚNIOR
#- Até 25 anos: SÊNIOR
#- Acima de 25 anos: MASTER

age = int(input('Digite ua idade: '))

if age <= 9:
    print('Voce tem {} anos, sua categoria e \033[0;30;42mMIRIM.\033[m'.format(age))
elif 14 >= age > 9:
    print('Voce tem {} anos, sua categoria e \033[0;30;42mINFATIL.\033[m'.format(age))
elif age <= 19 and age > 14:
    print('Voce tem {} anos, sua categoria e \033[0;30;42mJUNIOR.\033[m'.format(age))
elif 25 >= age > 19:
    print('Voce tem {} anos, sua categoria e \033[0;30;42mSENIOR.\033[m'.format(age))
else:
    print('Voce tem {} anos, sua categoria e \033[0;30;42mMASTER.\033[m'.format(age))
