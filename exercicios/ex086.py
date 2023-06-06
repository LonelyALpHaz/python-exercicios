#MATRIZ EM LISTAS:
matriz = [[0, 0], [0, 1], [0, 2],
          [1, 0], [1, 1], [1, 2],
          [2, 0], [2, 1], [2, 2]]
for pos, x in enumerate(matriz):
    num = int(input(f'Digite um valor para a posição {matriz[pos]}: '))
    matriz[pos].append(num)
print('-' * 45)
print(f'[ {matriz[0][2]:^3} ] [ {matriz[1][2]:^3} ] [ {matriz[2][2]:^3} ]\n'
      f'[ {matriz[3][2]:^3} ] [ {matriz[4][2]:^3} ] [ {matriz[5][2]:^3} ]\n'
      f'[ {matriz[6][2]:^3} ] [ {matriz[7][2]:^3} ] [ {matriz[8][2]:^3} ]')
print('-' * 45)
