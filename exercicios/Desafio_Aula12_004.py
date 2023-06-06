from datetime import date
ano = int(input('Em que ano você nasceu? '))
idade = date.today().year - ano
alistamento = 18
if idade < alistamento:
    print('Ainda não está na hora de você se alistar, você tem {} anos e para se alistar você precisa ter {} anos.'.format(idade, alistamento))
elif idade == alistamento:
    print('Chegou a hora! Você precisa se alistar esse ano.')
elif idade > alistamento:
    print('Você é mais velho do que a idade exigida para se alistar.')
