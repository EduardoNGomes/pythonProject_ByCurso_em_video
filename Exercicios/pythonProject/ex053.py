#Exercício Python 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
# desconsiderando os espaços

phrase = str(input('Digite um frase:')).strip().upper()
words = phrase.split()
union = ''.join(words)
reverse = ''
for letter in range(len(union) - 1 , -1, -1):
    reverse += union[letter]
if union == reverse:
    print('Temos um palindromo')
else:
    print('Nao e um palindromo')
    
