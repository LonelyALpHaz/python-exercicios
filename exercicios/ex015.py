#CARRO ALUGADO:
d = int(input(print('Dias alugados com o carro: ')))
k = float(input(print('Quantidade de km rodados: ')))
car = d * 60
kmr = k * 0.15
total = car + kmr
print('O total a pagar é R${:.2f}.'.format(total))
