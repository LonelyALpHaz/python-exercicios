#MAIOR E MENOR VALORES:
maior = menor = 0
v1 = int(input('Digite o primeiro valor: '))
v2 = int(input('Digite o segundo valor: '))
v3 = int(input('Digite o terceiro valor: '))
#MENOR VALOR:
if v1 < v2 and v1 < v3:
    menor = v1
if v2 < v1 and v2 < v3:
    menor = v2
if v3 < v1 and v3 < v2:
    menor = v3
#MAIOR VALOR:
if v1 > v2 and v1 > v3:
    maior = v1
if v2 > v1 and v2 > v3:
    maior = v2
if v3 > v1 and v3 > v2:
    maior = v3
print('O maior valor é {}.\nO menor valor é {}.'.format(maior, menor))
