def aumentar(v=0, t=0):
    return v + ((v/100) * t)


def diminuir(v=0,t=0):
    return v - ((v/100) * t)

def dobro(n=0):
    return n * 2

def metade(n=0):
    return n /2

def moeda(preco=0, moeda = 'R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')