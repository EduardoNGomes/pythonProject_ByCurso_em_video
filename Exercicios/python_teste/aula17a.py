#Listas

#num = [2,5,9,1]
#num[2] = 3
#num.append(7) Adicionando a lista.
#num.insert(2,0) Adicionando elemento 0 na posicao 2.
#num.sort() Organizando a lista.
#num.pop() Remove o ultimo elemento da lista.
#num.pop(2) Remove o elemento de indice 2.
#num.remove(2) Remove a primeira ocorrencia do valor passado por parametro.Se nao existe esta valor na lista ira  ocorrer error
#if 4 in num: Pesquisa se exite o valor solicitado na lista para decidir o que ira acontecer.
#   num.remove(4)
#else:
#    print('Nao ha valor 4')


#num.sort(reverse=True)Organizando do ultimo elemento para o primeiro.
#print(f'Essa lista tem {len(num)} elementos.') Retornando quantidade de elementos da lista len(num).

valores = []
for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))

for c,v in enumerate(valores):
    print(f'Na posicao {c} esta o valor {v}')


# a = [2,4,5,8]
# b = a Cria uma LIGACAO de 'a' dentro de 'b'
# b = a[:]  Cria uma COPIA de 'a' dentro de 'b'
# b[2] = 8
# print(f'Lista A: {a}')
# print(f'Lista B : {b}}')  
#