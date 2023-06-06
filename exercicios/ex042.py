#CONDIÇÃO DE EXISTÊNCIA DE UM TRIÂNGULO V 2.0:
a = float(input('Primeira medida: '))
b = float(input('Segunda medida: '))
c = float(input('Terceira medida: '))
if a + b > c and b + c > a and c + a > b:
    print('Com essas medidas É POSSÍVEL formar um triângulo ', end='')
    if a == b == c:
        print('EQUILÁTERO.')
    elif a != b != c != a:
        print('ESCALENO.')
    else:
        print('ISÓCELES.')
else:
    print('Com essas medidas NÃO É POSSÍVEL formar um triângulo.')
