#CALCULO DA HIPOTENUSA DE UM TRIÂNGULO:
from math import hypot
co = float(input(print('Comprimento do cateto oposto: ')))
ca = float(input(print('Comprimento do cateto adjacente: ')))
r = hypot(co, ca)
print('Sabendo que os valores dos catetos, respectivamente, são {} e {}, o valor da hipotenusa é {:.2f}.'.format(co, ca, r))
