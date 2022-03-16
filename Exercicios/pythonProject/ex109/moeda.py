def aumentar(v=0, t=0, formato=False):
    res = v + ((v/100) * t)
    return res if formato is False else moeda(res)


def diminuir(v=0,t=0, formato=False):
    res = v - ((v/100) * t)
    return res  if formato is False else moeda(res)


def dobro(n=0, formato=False):
    res = n * 2
    return res  if formato is False else moeda(res)


def metade(n=0, formato=False):
    res = n /2
    return res  if formato is False else moeda(res)


def moeda(preco=0, moeda = 'R$',):
    return f'{moeda}{preco:.2f}'.replace('.', ',')