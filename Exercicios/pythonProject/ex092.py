#Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime       #Importando biblioteca para usar o ano atual para saber a idade
pessoa = dict()                     #Dicionario vazio

pessoa['nome'] = str(input('Nome: '))           #Adicionando nome ao elemento ['nome'].
anoN = int(input('Ano de nascimento: '))        #Adicionando ano de nascimento a uma variavel qualquer.
age = datetime.today().year - anoN              #Subtraindo o ano atual da variavel que armazena ano do nascimento e add a outra variavel.
pessoa['idade'] = age                           #Adicionando variavel age ao elemento ['idade'].
pessoa['ctps'] =  int(input('Carteira de trabalho (0 nao tem): '))      # Adicionado ctps ao elemento ['ctps'].
if pessoa['ctps'] == 0:                         #Verificando se ctps e igual a zero.
    print('=='*20)
    for k,v in pessoa.items():                  #Loop para listar todas as keys(k) e values(v) do dicionario pessoa(pessoa.items()).
        print(f'{k} tem o valor {v} ')

else:                                                               #Continuacao caso ctps for diferente de zero.
    pessoa['contratacao'] = int(input('Ano de contratacao: '))      #Adicionando ano de contratracao ao elemento ['contratacao']
    pessoa['salario'] = float(input('Salaraio: R$ '))               #Adicionando salario ao elemento ['salario']
    pessoa['aposentadoria'] = 70 - age                              #Adicionando 70 - a variavel age ao elemento ['aposentadoria']
    print('=='*20)
    for k,v in pessoa.items():                                      #Loop para listar todas as keys(k) e values(v) do dicionario pessoa(pessoa.items()).
        print(f'{k} tem o valor {v}')

    
    


