#Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

aluno = dict()

aluno['nome'] = str(input('Nome: '))
aluno['media'] = int(input(f'Media de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['Situacao'] = 'Aprovado'
elif aluno['media'] >= 5:
    aluno['status'] = 'Recuperacao'
else:
    aluno['status'] = 'Repovado'

print('=='*15)

for k,v in aluno.items():
    print(f'{k} e igual a {v}')