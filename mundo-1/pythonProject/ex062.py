#Exercício Python 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.


firstTerm = int(input('Primeiro Termo: '))
reason = int(input('Razao: '))
count = 0
term = firstTerm
countAux = 10
while count < 10:
    print('{} → '.format(term),end='')
    term += reason
    count += 1
    if count == 10:
        choice = int(input('Aguardando...\nDigite mais um termo ou 0 para finalizar o programa: '))
        if choice == 0:
            print('Finalizando...')
            count = 10
        else:
            count = count - choice
            countAux += choice
print('Progressao finalizada com \033[42m{} termos\033[m mostrados'.format(countAux))
