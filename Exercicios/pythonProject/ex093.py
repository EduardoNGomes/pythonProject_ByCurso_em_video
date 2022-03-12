#Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

dados = dict()                                                  #Criando um dicionario vazio.

dados['nome'] = str(input('Nome do jogador: '))                 #Adicionando o nome ao elemento (nome).
ngame = int(input('Quantas partidas ele jogou: '))              #Adicionando a qtde de jogos a uma variavel para usar como contador nos loops.
if ngame == 0:                                                  #Verificando se a variavel e igual a zero para continuar ou nao o programa. 
    print(f'O jogador {dados["nome"]} nao entrou em campo.') 
else:
    listgols = list()                                           #Criando uma lista vazia para armazenar os gols. 
    totalgoals = 0                                              #Criando uma variavel para contar o total de gols.
    c = d = 1                                                   #Variveis para serem usadas como contador.

    while c <= ngame:                                           #Iniciando o loop enquanto a variavel de contagem for menor ou igual que o numero de jogos.
        gols = (int(input(f'Quantos gols na partida {c}: ')))   
        totalgoals += gols                                      #Realizando a contagem total de gols.
        listgols.append(gols)                                   #Adicionando o numero de gols a lista(listgols).
        c +=1                                                   #Incrementacao da variavel de contagem.

    dados['gols'] = listgols[:]                                    #Adicionando a lista de gols(listgols) ao dicionario(dados).
    dados['total'] = totalgoals                                 #Adicionando a contagem total de gols(total) ao dicionario(dados).

    print('-='*30)
    print()

    print(dados)                                                #Mostrando dicionario dados sem formatacao alguma..

    print('-='*30)
    print()

    for k,v in dados.items():                                   #Mostrando os dados por keys(k) e values(v)
        print(f'O campo {k} tem o valor {v}')

    print('-='*30)
    print()

    print(f'O jogador {dados["nome"]} jogou {ngame} partidas.')#Informando a qtde de partidas(ngame) realizadas pelo jogador(dados[nome])
    while d <= ngame:                                          #Iniciando o loop enquanto a variavel de contagem for menor ou igual que o numero de jogos.
        print(f'→Na partida {d}, fez {dados["gols"][d-1]} gols')# Informando nr de partida com a varivel[d] e nr de gols com (dados['gols'][d-1]) pois o primeiro (d) tem indice 1 e o primeiro gols tem indice 0  
        d +=1                                                  #Incrementacao da variavel de contagem.
    print(f'Foi um total de {dados["total"]}')                 #Informando total de gols(dados['total'])

