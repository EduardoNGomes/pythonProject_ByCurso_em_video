#Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

#- Quantidade de notas
#- A maior nota
#- A menor nota
#- A média da turma
#- A situação (opcional)

#Adicione também as docstrings dessa função para consulta pelo desenvolvedor.

def notas(* num, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param num: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situacão da turma

    """
    

    nt = {}

    nt['total'] = len(num)
    nt['maior nota'] = max(num)
    nt['menor nota'] = min(num)
    nt['media'] = sum(num) /len(num)
    if sit == True:
        if nt['media'] >  7:
            nt['situacao'] = 'boa'
        elif nt['media'] > 6:
            nt['situacao'] = 'razoavel'
        else:
            nt['situacao'] = 'ruim'
    return nt 



resp = notas(5,5.2,6, sit=True)
print(resp)