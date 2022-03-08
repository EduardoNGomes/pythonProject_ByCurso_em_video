#Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#- EQUILÁTERO: todos os lados iguais
#- ISÓSCELES: dois lados iguais, um diferente
#- ESCALENO: todos os lados diferentes

s1 = int(input('Digite o primeiro segmento: '))
s2 = int(input('Digite o segundo segmento: '))
s3 = int(input('Digite o terceiro segmento: '))

if s1 + s2 > s3 and s1 + s3 > s2 and s3+s1 > s2:
    print('Os segmentos podem formar um triangulo')
    if s1==s2 and s2==s3 and s3==s1:
        print('O triangulo e EQUILATERO')
    elif s1 == s2 or s2 == s3 or s3 == s1:
        print('O triangulo e ISOCELES')
    elif s1 != s2 and s2 != s3 and s3 != s1:
        print('O trianfulo e ESCALENO')

else:
    print(('Os segmentos NAO podem formar um triangulo'))
