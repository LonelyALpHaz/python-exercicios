#SOMA DE ÍMPARES MÚLTIPLOS DE 3:
# s = acumulador
# c = contador
s = 0
c = 0
for a in range(1, 501):
    if a % 3 == 0 and a % 2 != 0:
        s += a
        c += 1
print('A somatória de todos os {} números ímaperes divisíveis por 3 entre 1 e 500 é igual a {}.'.format(c, s))
