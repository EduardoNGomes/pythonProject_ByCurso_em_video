#Aula 20 Funcoes(Parte 1)

def titulo(txt):                    #Criando uma funcao passando TXT como parametro
    print('-'*20)                   
    print(txt)
    print('-'*20)

#SOMANDO VALORES PASSADOS POR PARAMENTROS
def soma(a, b):                     #Criando uma funcao passando A , B por parametro
    print(f'A = {a} e B = {b}')     #Mostrando qual sera A e qual sera B    
    s = a+b                         #Realizando a soma entre os parametros 
    print(f'A soma A + B = {s}')    #Mostrando o resultado da soma


def contador(* num):                                        #Guardando uma qtde de numeros que sera passado por parametro
    tam = len(num)                                          #Armazendo a qdte ao todo de numeros
    print(f'Recebi os valores {num} e sao {tam} numeros')   #Mostrando quais foram os numeros e qual a qdte.


def desempacota(* valores):                                 #Guardando uma qtde de numeros que sera passado por parametro
    s = 0
    for num in valores:                                     #Loop para fazer algo com cada numero passado commo parametro
        s += num                                            #Realizando a soma dos numeros
    print(f'Somando os valores {valores} temos {s}')        #Mostrando os numeros passados e a soma deles


def dobra(list):                                            #Definindo a funcao dobra com um parametro
    pos = 0                                     
    while pos < len(list):                                  #Loop para realizar algo enquando o valor for menor que o tamanho da lista 
        list[pos] *=2                                       #Dobrando o valor de cada item na lista
        pos += 1                                            #Condicao de saida do loop



#Programa principal
titulo('Curso em Video')            #Chamando a funcao passando qual mensagem sera usada como parametro
titulo('Python e muito BOM!')       #Chamando a funcao passando qual mensagem sera usada como parametro
titulo('Oi')                        #Chamando a funcao passando qual mensagem sera usada como parametro


soma(b=4,a=5)                       #Realizando a funcao soma com os parametro a=5 e b=4
soma(7,2)                           #Realizando a funcao soma com os valores 7 e 2


contador(2,7,1)                     #Passando valores para a funcao contador
contador(8,0)                       #Passando valores para a funcao contador
contador(4,4,7,6,2)                 #Passando valores para a funcao contador

desempacota(5,2)                    #Chamando funcao desempacota passando 5 e 2 como parametro
desempacota(2,9,4)                  #Chamando funcao desempacota passando 2, 9 e 4 como parametro


valores = [6,0,8,1,2,3]             #Criando uma lista
dobra(valores)                      #Chamando a funcao dobra com o parametro(valores)
print(valores)                      #Exibindo o valores apos a realizacao da funcao dobra