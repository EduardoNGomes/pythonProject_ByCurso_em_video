#Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.



def voto(dob):
    from datetime import datetime

    age = datetime.today().year - dob
    
    if age >= 65:
        return f'Voec possui {age} anos. VOTO OPCIONAL'
    elif age >= 18:
        return f'Voce possui {age} anos. VOTO OBRIGATORIO'
    elif age >= 16:
        return f'Voce possui {age} anos. VOTO OPCIONAL'
    else:
        return f'Voce possui {age} anos. VOTO NEGADO'

n = int(input('Qual seu ano de nascimento? '))
print(voto(n))