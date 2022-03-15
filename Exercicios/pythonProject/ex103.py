#Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.


def ficha(nome = 'desconhecido',gols=0 ):                           #Criando a funcao ficha()
        return f'O jogador {nome} fez {gols} gols no campeonato.'   #Retornado os dados do jogador



name = str(input('Nome do jogador: ')).strip()                      #Adicionando o nome a veriavel removendo os espacos vazio,caso haja
if name == '':                                                      #Verificando se nome esta vazio
    name = 'desconhecido'                                           #Atribuindo 'desconhecido' a variavel
goal = str(input('Numero de goals: '))                              #Adicionado qdte em forma de str para nao dar erro caso seja vazia

if goal.isnumeric():                                                #Verificando se a variavel goal e um numero
    print(ficha(name,goal))                                         #chamando a funcao ficha passando duas variaveis como parametro
else:
    goal = 0                                                        #se goal nao for m numero vai recever o valor 0
    print(ficha(name,goal))
