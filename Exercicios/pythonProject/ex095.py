#Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.


jogadores = list()
gols = list()
dados = dict()
ngame = 0

#loop para obter dados
while True:
    dados.clear()                                                   #Zerando dicionario[dados].
    gols.clear()                                                    #Zerando lista[gols].
    dados['nome'] = str(input('Nome do jogador: '))                 #Adicionado [value]nome para a key[nome].
    ngame = int(input(f'Quantas partidas {dados["nome"]} jogou? ')) #Recebendo variavel para saber qtde de jogos para realizar o loop.
    for c in range(0,ngame):                                        #Loop para saber qtde de gols em cada partida(ngame)
        gols.append(int(input(f'Quantos gols na partida {c+1}? '))) #Adicionando a qtde de gols a lista[gols]
        dados['gols'] = gols[:]                                     #Clonando a lista[gols] para o dicionario[gols]
    jogadores.append(dados.copy())                                  #Clonando todos os dados obtidos[dados] para a lista[jogadores]

#loop para condicao de saida do LOOP GERAL
    while True:                                                     #loop para condicao de saida 
        answer = str(input('Deseja continuar ? [S/N] ')).strip()[0] #Armazenando resposta na variavel(answer)
        if answer in 'SsNn':                                        #Verificando se a resposta esta dentro do parametro esperado    
            break                                                   #Caso a resposta esteja no parametro esperando ira sair do loop
        else:                                                       #Senao
            print('\033[41mOPCAO INVALIDA\033[m')                   #Informara que a resposta nao esta correta
    if answer in 'Nn':                                              #Se resposta for N
        break                                                       #Saindo do loop geral


#APENAS FORMATACAO
print('='*40)
print('Cod',end='')
print('      Nome',end='')
print('           gols',end='')
print('             total')
print('-'*40)


#Exibindo Lista com todos os elementos armazenados
for i,v in enumerate(jogadores):
    print(f'{i}        {v["nome"]}            {v["gols"]}        {sum(v["gols"])}')

#LOOP para saber se o usuario deseja mostrar dados adicionais
while True:
    answer = str(input('Deseja mostrar dados adicionais [S/N]? ')).strip()[0]           #Verificando se a resposta esta dentro do parametro esperado  
    if answer in 'Ss':                                                                  
        showdados = int(input('Mostrar dados de qual jogador[COD ou 999 para sair]?'))  #Armazenado o indicice digitado pelo usuario em uma variavel
        if showdados == 999:
            break
        if showdados >= len(jogadores):
            print('OPCAO INVALIDA')
        else:    
            print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[showdados]["nome"]}')             #Exibindo o nome do usuario usando o indice na lista (jogadore[showdados]["nome"])
            for c in range (0, len(jogadores[showdados]["gols"])):                          #Loop para exibir a qtde de gols usando o tam total gols armazenados (len(jogadores[showdados]["gols"]))
                print(f'No jogo {c+1} fez {jogadores[showdados]["gols"][c]} gols.')         #Exibindo usando c+1 pois c comeca em 0 e o item armazenado em jogadores['gols'] no indice que esta o c com jogadores[showdados][c]
    else:                                                                               
        if answer in 'Nn':                                                              #condicao de saindo do Loop
             break
        else:
            print('\033[41mOPCAO INVALIDA\033[m')


