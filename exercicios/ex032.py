#ANO BISSEXTO:
from datetime import date
a = int(input('Informe um ano para saber se ele é ou não bissexto, se for o ano atual basta digitar "0": '))
if a == 0:
    a = date.today().year
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('O ano {} é bissexto.'.format(a))
else:
    print('O ano {} não é bissexto.'.format(a))
