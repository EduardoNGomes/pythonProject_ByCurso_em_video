#Dicionario

estado = dict()     #Criando um dicionario vazio
brasil = list()     #Criando uma lista vazia    

for c in range(0,3):        #loop
    estado['uf'] = str(input('Unidade Federal: '))      #Criando e armazenado elemento no dicionario
    estado['sigla'] = str(input('Sigla do Estado'))     #Criando e armazenando elemento no dicionar
    brasil.append(estado.copy())        #Copiando Elemento armazenado ao dicionario para a Lista

for e in brasil:    #Loop para exibir todos os arquivos salvos na lista
    for v in e.value:   #Exibindo todos os arquivos em dicionario.
        print(v, end= ' ')
    print()

    