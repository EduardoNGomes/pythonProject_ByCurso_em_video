#Exercício Python 114: Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://youtube.com.br')
except urllib.error.URLError:
    print('O site nao esta disponivel no momento')
else:
    print('O site esta funcionando normalmente')