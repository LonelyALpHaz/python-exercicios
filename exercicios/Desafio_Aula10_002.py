v = int(input('Qual a velocidade do carro? Km/h '))
multa = (v - 80) * 7
if v > 80:
    print('Você ultrapassou o limite de velocidade, a multa a ser paga é de R${}.'.format(multa))
else:
    print('Você não foi multado, pois não excedeu o limite de 80Km/h.')
