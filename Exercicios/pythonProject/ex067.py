#Exercício Python 067: Faça um programa que mostre a tabuada de vários números, um de cada vez,
# para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

while True:
    number = int(input('Deseja ver a tabuada de qual valor? '))
    if number <= 0:
        break
    count = 1
    while count <=10:
        print(f'{number} x {count} = {number*count}')
        count +=1
