import math
num = float(input('Digite um angulo '))
sin = math.sin(math.radians(num))
cos = math.cos(math.radians(num))
tan = math.tan(math.radians(num))
print(' O angulo de {} tem o SENO de {:.2f}\n O COSSENO de {:.2f}\n A TAGENTE de {:.2f} '.format(num, sin, cos,tan))
