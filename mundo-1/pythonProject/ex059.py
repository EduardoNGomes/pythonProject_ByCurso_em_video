#Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.

n1 = float(input('Digite o primeiro numero: '))
n2 = float(input('Digite o segundo numero: '))

option = 0
while option != 5:
    print('''
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa
    ''')
    option = int(input('Qual sua escolha? '))
    if option == 1:
        print('O resultado da \033[44mSOMA\033[m dos numeros e {}'.format(n1+n2))
        print('=='*30)
    elif option == 2:
        print('O produto da \033[44mMULTIPLICACAO\033[m dos numeros e {}'.format(n1 * n2))
        print('==' * 30)
    elif option == 3:
        if n1 > n2:
            print('O \033[44mMAIOR\033[m numero digitado foi {}'.format(n1))
            print('==' * 30)
        else:
            print('O \033[44mMAIOR\033[m numero digitado foi {}'.format(n2))
            print('==' * 30)
    elif option == 4:
        n1 = float(input('Digite outro numero: '))
        n2 = float(input('Digite outro numero: '))
        print('==' * 30)
    elif option < 1 or option >= 6 :
        print('Opcao \033[41mINVALIDA\033[m')
        print('==' * 30)
print('\033[7mPROGRAMA ENCERRADO\033[m')
