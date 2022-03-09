#Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente. 


valores = []

while True:
    valores.append(int(input('Digite um valor para ser acrescentado na lista: ')))# Adicionando valores a lista
    if len(valores) == 1 or valores[-1] not in valores[:-1]:# Testando se foi o primeiro numero digitado, ou se nao possui numero igual na lista.
        print('\033[42mValor adicionado\033[m')
    else:
        for v in valores:# Analisando todos os valores na lista
            if valores[-1] in valores[:-1]: #Se ultimo valor da lista ja existe 
                valores.pop(-1)             #ira executar o comando POP(-1)
                print('\033[41mValor ja existente! Escolha outro.\033[m')
    answer = str(input('Deseja Continuar [S/n]? ')).strip()[0]
    if answer not in 'Ss':
        if answer in 'Nn':
            break
        else:
            print('\033[41mOpcao Invalida\033[m')
print(f'Os valores digitados foram {sorted(valores)}')#Colocando valores de forma crescente com o comando sorted()
