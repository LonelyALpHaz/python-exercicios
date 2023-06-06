#MAIOR E MENOR PESO:
maior = 0
menor = 0
for a in range(1, 6):
    peso = float(input('Qual o peso da {}ª pessoa? '.format(a)))
    lista = [peso]
    for b in lista:
        if maior == 0 or b > maior:
            maior = b
        if menor == 0 or b < menor:
            menor = b
print('=' * 24)
print('O maior peso é {}Kg.\nO menor peso é {}Kg.'.format(maior, menor))
print('=' * 24)
