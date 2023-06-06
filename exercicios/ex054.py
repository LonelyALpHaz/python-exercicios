#GRUPO DA MAIORIDADE:
from datetime import date
maior = 0
menor = 0
atual = date.today().year
for c in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    idade = atual - nasc
    if idade >= 21:
        maior += 1
    elif idade < 21:
        menor += 1
print('De acordo com as idades nós temos...\n{} pessoas na maioridade.\n{} pessoas menores de idade.'.format(maior, menor))
