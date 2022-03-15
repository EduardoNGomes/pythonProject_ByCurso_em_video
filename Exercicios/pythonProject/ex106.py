#Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará.


def ajuda(v):
    return help(v)


while True:
    print('-=-'*10)
    print('SISTEMA DE AJUDA PyHelp')
    print('-=-'*10)
    answer = str(input('[mFuncao ou Biblioteca: '))
    if answer == 'fim':
        break
    else:
        ajuda(answer)
    

