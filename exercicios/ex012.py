#CÁLCULO DO DESCONTO:
p = float(input(print('Valor do produto: ')))
d = float(input(print('Valor do desconto: ')))
des = (p * d) / 100
total = p - des
print('Com um desconto de 5% o valor do produto fica {:.2f}'.format(total))
