def soma(a=0,b=0,c=0):                              #Criacao da funcao soma passando parametro opcionais
    s = a+b+c                                       #variavel s recebendo a soma dos parametros 
    return s                                        #Retornando s


r1 = soma(3,2,5)                                    #Variavel r1 recebe os resultado da funcao soma com os parametros passados
r2 = soma(2,2)                                      #Variavel r2 recebe os resultado da funcao soma com os parametros passados
r3 = soma(6)                                        #Variavel r3 recebe os resultado da funcao soma com os parametros passados

print(f'Os resultados foram {r1}, {r2}, {r3}')      #Imprimindo os resultado armazenados nas variaves r1 r2 r3.

