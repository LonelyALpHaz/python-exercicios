s = 0
for c in range(1, 501):
    if c % 3 == 0 and c % 2 != 0:
        s += c
print('A somatória de todos os números ímaperes divisíveis por 3 é igual a {}.'.format(s))



