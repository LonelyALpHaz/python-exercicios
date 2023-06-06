#ÁREA DE UM TERRENO:
def area(l, c):
    a = l * c
    print(f'{a:.1f}m²')


def mensagem(msg):
    print(msg, end='')


def lin():
    print('-' * 28)
    print(f'{"CONTROLE DE TERRENO":^28}')
    print('-' * 28)


lin()
l = float(input('- Largura do terreno (m): '))
c = float(input('- Comprimento do terreno (m): '))
mensagem(f'O seu terreno mede {l:.2f}x{c:.2f}m e a área é de ')
area(l, c)
