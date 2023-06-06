#CUSTO DA VIAGEM:
n = int(input('Qual a distância da sua viagem? Km '))
mepass = n * 0.50
mapass = n * 0.45
if n < 200:
    print('O valor da passagem é de R${:.2f}.'.format(mepass))
else:
    print('A viagem excedeu o limite de 200 Km, então a passagem será R${:.2f}.'.format(mapass))
