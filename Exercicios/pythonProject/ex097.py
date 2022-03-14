#Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

def escreva(txt):                   #Criando a funcao escreva
    print('-'*(len(txt)+4))         #Apenas formatacao de acordo com a qdt de letras que o parametro possui
    print(f'  {txt}')               #Exibindo o parametro
    print('-'*(len(txt)+4))         #Apenas formatacao de acordo com a qdt de letras que o parametro possui


escreva('Ola, mundo')               #Chamando funcao passando o parametro
escreva('Oi')                       #Chamando funcao passando o parametro