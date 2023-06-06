#CÁLCULO DO GASTO EM l DE TINTA:
l = float(input(print('Largura da parede: ')))
a = float(input(print('Altura da parede: ')))
area = (l * a)
print('A sua parede tem uma dimensão de {}x{} e a área é igual a {}m².'.format(l, a, area))
tinta = (area / 2)
print('Para pintar essa parede serão necessários {} litros de tinta.'.format(tinta))
