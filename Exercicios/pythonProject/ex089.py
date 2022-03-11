#Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

boletim = []
aluno = []

while True:
    aluno.append(str(input('Nome: '))) # Colocando elemento em lista  ALUNO[0]
    aluno.append(float(input('Nota 1: ')))  # Colocando elemento em lista  ALUNO[1]
    aluno.append(float(input('Nota 2: '))) # Colocando elemento em lista  ALUNO[2]

    boletim.append(aluno[:])    #CLONANDO lista  ALUNO para lista BOLETIM
    aluno.clear()   #ZERANDO lista ALUNO para nao haver duplicacao  



    answer = str(input('Deseja continuar[S/N]? ')).strip()[0]   #Condicao de saide do loop WHILE
    if answer not in 'Ss':
        if answer in 'Nn':
            break
        else:
            print('OPCAO INVALIDA')
print('='*30)

print('No.  ',end='')   #APENAS FORMATACAO
print('Nome       ', end='')#APENAS FORMATACAO
print('  Media')#APENAS FORMATACAO
print('-'*15)#APENAS FORMATACAO

for i,p in enumerate(boletim):# Verficando todos os elementos em BOLETIM 
    print(f' {i}   {p[0]}       {(p[1]+p[2])/2}') # Listando INDICE = (i)  |NOME do aluno = (p[0]) |MEDIA = (p[1](primeira nota) + p[2](segunda nota)) /2
print('-'*30)


while True:
    answer2 = str(input('Deseja mostrar as notas de algum aluno? ')).strip()[0]# Condicao de saida do loop WHILE
    if answer2 in 'Ss':
        nraluno = int(input('Qual o numero do aluno? ')) # Verficando numero do aluno = INDICE na lista BOLETIM
        if nraluno <= len(boletim)-1:
            print(f'Notas de {boletim[nraluno][0]} sao: {boletim[nraluno][1]}, {boletim[nraluno][2]}') # boletim[nraluno][0] = (Nome do aluno) | boletim[nraluno][1] = (primeira nota) |  boletim[nraluno][2] = (segunda nota)
        else:
            print('Opcao Invalida')
    else:
        if answer2 not in 'Nn':
            print('OPCAO INVALIDA')
        else:
            break
        