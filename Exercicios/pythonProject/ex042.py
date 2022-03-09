#Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
#calcule seu Índice de Massa Corporal (IMC) e
#mostre seu status, de acordo com a tabela abaixo:
#- IMC abaixo de 18,5: Abaixo do Peso
#- Entre 18,5 e 25: Peso Ideal
#- 25 até 30: Sobrepeso
#- 30 até 40: Obesidade
#- Acima de 40: Obesidade Mórbida

alt = float(input('Digite sua altura(metros): '))
weight = float(input('Digite seu peso(kg): '))

imc = weight / (alt**2)

if imc < 18.5:
    print('Seu indice de massa Corportal e {:.2f}'.format(imc))
    print('Voce esta \033[0;30;43mAbaixo do Peso\033[m')
elif imc <= 25:
    print('Seu indice de massa corporal e {:.2f}'.format(imc))
    print('Voce esta no \033[4;30;42mPeso Ideal\033[m')
elif imc <= 30:
    print('Seu indice de massa corporal e {:.2f}'.format(imc))
    print('Voce esta com \033[1;30;41mSOBREPESO\033[m')
elif imc <= 40:
    print('Seu indice de massa corporal e {:.2f}'.format(imc))
    print('Voce esta com \033[1;30;41mOBESIDADE\033[m')
else:
    print('Seu indice de massa corporal e {:.2f}'.format(imc))
    print('Voce esta com \033[1;30;41mOBESSIDADE MORBIDA\033[m')
