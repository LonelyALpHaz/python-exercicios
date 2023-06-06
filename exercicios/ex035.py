#CONDIÇÃO DE EXISTÊNCIA DE UM TRIÂNGULO V1.0:
a = float(input('Primeira medida: '))
b = float(input('Segunda medida: '))
c = float(input('Terceira medida: '))
if a + b > c and b + c > a and a + c > b:
    print('\033[1;30mCom essas medidas \033[1;32mÉ POSSÍVEL\033[m \033[1;30mmontar um triângulo.\033[m')
else:
    print('\033[1;30mCom essas \033[1;31mNÃO É POSSÍVEL\033[m \033[1;30mmontar um triângulo.\033[m')
