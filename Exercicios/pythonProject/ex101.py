#Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.



def voto(dob):                                                  #Criacao da funcao voto passando por parametro ano do nascimento(dob).
    from datetime import datetime                               #Importando biblioteca para sabe ano atual.

    age = datetime.today().year - dob                           #Calculando e armazenando idade.
    
    if age >= 65:                                               #Verificando a idade
        return f'Voec possui {age} anos. VOTO OPCIONAL'         #Retornando resposta de acordo com a idade
    elif age >= 18:                                             #Verificando a idade
        return f'Voce possui {age} anos. VOTO OBRIGATORIO'      #Retornando resposta de acordo com a idade
    elif age >= 16:                                             #Verificando a idade
        return f'Voce possui {age} anos. VOTO OPCIONAL'         #Retornando resposta de acordo com a idade
    else:                                                       #Verificando a idade
        return f'Voce possui {age} anos. VOTO NEGADO'           #Retornando resposta de acordo com a idade

n = int(input('Qual seu ano de nascimento? '))                  #Armazenado ano do nascimento
print(voto(n))                                                  #chamando a funcao voto passando ano do nascimento como parametro