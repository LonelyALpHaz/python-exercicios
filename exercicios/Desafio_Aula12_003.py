n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
print('Analisando esses dois números podemos saber que...')
if n1 > n2:
    print('O número {} é maior que o {}.'.format(n1, n2))
elif n2 > n1:
    print('O número {} é maior que {}.'.format(n2, n1))
elif n1 == n2:
    print('Ambos os números tem o mesmo valor.')
