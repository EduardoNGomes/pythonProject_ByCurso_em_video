#Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

num = []

for c in range(0,5):
    n = int(input('Digite um numero: '))
    if c == 0 or n > num[-1]: #Testando se e o primeiro elemento ou se o elemento e maior do que o ultimo elemento da lista.
        num.append(n)# Adicionando elemento na ultima posicao.
    else:
        pos = 0
        while pos < len(num):
            if n <= num[pos]: #Verificando se o elemento e menor ou igual elemento que esta na lista na posicao atual da variavel 'pos'.
                num.insert(pos,n) # Adicionando o elemento na posicao que esta o lacao no momento.
                break #Saindo do laco para nao se tornar um loop infinito. 
            pos +=1
print(num)
    

