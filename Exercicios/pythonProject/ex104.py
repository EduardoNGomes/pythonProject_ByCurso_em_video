#Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.

def leiaInt(msg):                                   #Criando funcao leiaInt() com um msg como parametro 
    ok = False                                      #variavel como condicao de saido do loop
    valor = 0
    while True:                                     #Loop para verificacao
        n = str(input(msg))                         #Exibindo msg e armazenando o que for digitado em forma de str
        if n.isnumeric():                           #Verificando se foi digitado um numero
            valor = int(n)                          #Transformando em numero
            ok = True                               #condicao de saido do loop
        else:
            print(f'\033[41mOPCAO INVALIDA\033[m')  #Caso nao tenhao sido um numero ira exibir uma mensagem de erro
        if ok:                                      #condicao de saido do loop
            break                                   #saida do loop
    return valor                                    #retornando o resultado

n = leiaInt('Digite um numero: ')                   #Chamando a funcao leiaInt e passando uma msg como parametro e armazendo  a resposta
print(f'Voce acabou de digitar o numero {n}')       #Exibindo a resposta