# Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(n, show=False):                     #Criando funcao fatorial
    """
        → Função para calcular o fatorial de um número
    :param n: número que terá o seu fatorial calculado
    :param show: se True, mostra a sequência do cálculo
    :return: impressão do resultado
    """
    f = 1                                        #Variavel de controle
    if show == True:                             #Verificando se a funcao tem o parametro show == True
        for c in range(n, 0, -1):                #Loop para calcular o fatorial   
            f *= c                               #Varivel de controle  fazendo o calculo necessario 
            if c == 1:                           #Quando o C for igual a 1 ira mostrar '=' apenas para FORMATACAO  
                print('1 ',end='= ')
            else:
                print(f'{c}',end= ' x ')        #Mostrando os valores de C para FORMATACAO  
        return f                                #Retornando o resultado
    else:
        for c in range(n, 0, -1):               #Loop para calcular o fatorial  
            f *= c                              #Varivel de controle  fazendo o calculo necessario 
        return f                                #Retornando o resultado



print(fatorial(5, True))                        #Chamando funcao fatorial passando 5 e True como parametros
print(fatorial(5))                              #Chamando funcao fatorial passando apenas 5 como parametro 
