#CLASSIFICAÇÃO DE UM COMPETIDOR:
from datetime import date
ano = int(input('Em que ano você nasceu? '))
idade = date.today().year - ano
if idade <= 9:
    print('O atleta que nasceu em {} tem {} anos.\nSua classificação é MIRIM.'.format(ano, idade))
elif idade > 9 and idade <= 14:
    print('O atleta que nasceu em {} tem {} anos.\nSua classificação é INFANTIL.'.format(ano, idade))
elif idade > 14 and idade <= 19:
    print('O atleta que nasceu em {} tem {} anos.\nSua classificação é JÚNIOR.'.format(ano, idade))
elif idade > 14 and idade <=25:
    print('O atleta que nasceu em {} tem {} anos.\nSua classificação é SÊNIOR.'.format(ano, idade))
elif idade > 25:
    print('O atleta que nasceu em {} tem {} anos.\nSua classificação é MASTER.'.format(ano, idade))
