#Exercício Python 115a: Vamos criar um menu em Python, usando modularização.

from turtle import st
from util.interface import *
from util.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)


while True: 
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        #Opcao de lista o conteudo de um arquivo
        lerArquivo(arq)

    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do sistema... Ate logo')
        break
    else:
        print('\0033[31mERRO!Digite uma opcao valida.\033[m')
        sleep(1)