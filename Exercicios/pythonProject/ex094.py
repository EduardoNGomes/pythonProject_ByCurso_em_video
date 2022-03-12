#Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
#A) Quantas pessoas foram cadastradas
#B) A média de idade
#C) Uma lista com as mulheres
#D) Uma lista de pessoas com idade acima da média


dadosgeral = list()             #Criacao da lista principal 
dados = dict()                  #Criacao do dicionario
mediaIdade = idadetotal = 0     #Variaveis para realizacao das contas   
nameWoman = list()              #Lista para nome das mulheres

#Armazenando Informacoes
while True:                                                         #Loop para armazenar dados no dicionario
    dados['nome'] = str(input('Nome: '))                            #Armazenando elemento ['nome'] no dicionario [dados]
    while True:                                                     #Loop para validar resposta sobre o sexo
        dados['sexo'] = str(input('Sexo [M/F]: ')).strip()[0]       #Armazenado o elemento ['sexo'] no dicionario [dados]
        if dados['sexo'] in 'Mmff':                                 #Validacao para o sexo
            break                                                   
        print('\033[41mERRO!\033[m Por favor, digite apenas M / F') #Erro para sexo invalido
    dados['idade'] = int(input('Idade: '))                          #Armazenando elemento ['idade'] no dicionario [dados]
    dadosgeral.append(dados.copy())                                 #Copiando dados do dicionario [dados] para a lista [dadosgeral]
    while True:                                                     #Loop para validar resposta sobre o sobre continaur adicionando pessoas
        answer = str(input('Quer continuar? ')).strip()[0]          #Armazendo a resposta de continuar ou nao
        if answer in 'SsNn':                                        #Saindo do primeiro loop se a resposta for Ss / Nn
            break
        print('\033[41mOPCAO INVALIDA\033[m')                       #Erro para resposta invalida
    if answer in 'Nn':                                              #Saindo do loop principal de armazenamento de dados se a resposta for Nn
        break

#Total de pessoas
print(f'A) Ao todo temos {len(dadosgeral)} pessoas.')

#Calculando media de idade
for i,d in enumerate(dadosgeral):
    idadetotal += d['idade'] 

mediaIdade = idadetotal/len(dadosgeral)
print(f'B) A media de idade e de {mediaIdade} anos.')

#Quantidade de mulheres cadastradas
for d in dadosgeral:
    if d['sexo'] == 'f':
        nameWoman.append(d['nome'])
for i,woman in enumerate(nameWoman):
    if i == 0:
        print(f'C) As mulheres cadastradas foram: {woman}', end=' ')
    else:
        print(woman, end=' ')
print()

#Pessoas acima da media de idade
print(f'D) Lista das pessoas que estao acima da media:')
for d in dadosgeral:
    if d['idade'] > mediaIdade:
        print(f'       nome = {d["nome"]}; sexo = {d["sexo"]}; idade = {d["idade"]} ')
print('\033[7m<< Encenrando >>\033[m')