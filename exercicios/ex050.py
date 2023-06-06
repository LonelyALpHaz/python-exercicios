#SOMA DE NÚMEROS PARES:
print('Me informe 6 números, irei somar apenas os PARES, os ímpares serão DESCARTADOS.\n ' '')
s = 0
c = 0
for c in range(1, 7):
    num = int(input('Digite o {}° número: '.format(c)))
    if num % 2 == 0:
        s += num
        c += num
print('A soma de {} números pares é igual a {}.'.format(c, s))
