#ALISTAMENTO MILITAR:
from datetime import date
ano = int(input('Em que ano você nasceu? '))
anoatual = date.today().year
idade = date.today().year - ano
alistamento = 18
if idade < alistamento:
    print('Quem nasceu em {} tem {} anos em {}. Ainda faltam {} anos para você se alistar no exército. Você deverá se alistar em {}.'.format(ano, idade, anoatual, (alistamento - idade), (alistamento - idade + anoatual)))
elif idade == alistamento:
    print('Quem nasceu em {} tem {} anos em {}, você deve ir se alistar IMEDIATAMENTE!'.format(ano, idade, anoatual))
elif idade > alistamento:
    print('Quem nasceu em {} tem {} anos em {}. Você deveria ter se alistado em {}.'.format(ano, idade, anoatual, (alistamento - idade + anoatual)))
