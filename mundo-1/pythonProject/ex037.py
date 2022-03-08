#Exercício Python 037: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher
#qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.


n = int(input('Escolha um numero: '))
print(('''Deseja converter para qual base?
\033[0;30;42m| 1 - Binario |\033[m
\033[0;30;42m| 2 - Octal |\033[m
\033[0;30;42m| 3 - Hexadecimal |\033[m
 '''))

choice = int(input('Sua escolha: '))

if choice == 1:
    print('O numero escolhi foi {}, sua conversao em Binario e {}'.format(choice, bin(n)[2:]))

elif choice == 2:
    print('o numero escolhi foi {}, sua conversao em Octal e {}'.format(choice, oct(n)[2:]))
elif choice == 3:
    print('O numero escolhi foi {}, sua conversao para Hexadecimal e {}'.format(choice, hex(n)[2:]))
else:
    print('O numero {} nao e \033[0;30;41mvalido\033[m'.format(choice))
