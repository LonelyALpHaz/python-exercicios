#SENO, COSSENO E TANGENTE:
from math import sin, cos, tan, radians
n = float(input(print('Digit o ângulo que você deseja: ')))
rad = radians(n)
sin = sin(rad)
cos = cos(rad)
tan = tan(rad)
print('O seno do ângulo {} é {:.2f} \nO cosseno do ângulo {} é {:.2f} \nA tangente do ângulo {} é {:.2f}'.format(n, sin, n, cos, n , tan))
