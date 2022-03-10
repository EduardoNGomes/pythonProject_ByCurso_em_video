#Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.


exp = str(input('Digite sua expressao: '))# Adicionando a expressao na variavel.

qtdeP = [] # Array criado para armazenar a quantidade de parenteses.

for item in exp: # Loop percorrendo todos os elementos da expressao.
    if item == '(': # Verificando se no array possui um parenteses abrindo.
        qtdeP.append(item)# Adicionando esse numero no array de PARENTESES.
    elif item == ')':# Verificando se no array possui um parenteses fechando.
        if len(exp) > 0: # Se o a qtde de parenteses fechando for maior que 0,no A P, significa que os formaram um par.
            qtdeP.pop() # remove item do A P.
        else:
            qtdeP.append(item) 
            break

if len(qtdeP) == 0:# Se o valor terminar em 1, significa que exite um Parentese a mais, logo a expressao esta incorreta.
    print('\033[42mSua expressao esta correta!\033[m')
else:
    print('\033[41mSua expressao esta incorreta!\033[m')

