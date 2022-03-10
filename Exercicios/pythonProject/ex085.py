#Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.


num = [[],[]]# Criando uma unica lista que possui outra lista dentro dela

for c in range(1,8):# Iniciando loop
    n = int(input('Numero: '))
    if n % 2 == 0:# Verificando se o valor e par
        num[0].append(n)# Adicionando o valor par a lista(num) no indice 0
    else :
        num[1].append(n)# Adicionando o valor impar a lista(num) no indice 1

print(f'Os valores pares sao: {sorted(num[0])}')# Organizando os valores do menor para o maior
print(f'Os valores impares sao: {sorted(num[1])}')# Organizando os valores do menor para o maior