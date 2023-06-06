#DADOS EM UMA MATRIZ:
par = maior = 0
matriz = [[0, 0], [0, 1], [0, 2],
          [1, 0], [1, 1], [1, 2],
          [2, 0], [2, 1], [2, 2]]
for pos, x in enumerate(matriz):
    num = int(input(f'Digite um valor para a posição {matriz[pos]}: '))
    matriz[pos].append(num)
#SOMA DOS VALORES PARES:
    if num % 2 == 0:
        par += num
#MAIOR NÚMERO DA SEGUNDA LINHA:
matrizlist = [matriz]
for matriz in matrizlist:
    if matriz[3][2] == 0 or matriz[3][2] > maior:
        maior = matriz[3][2]
    if matriz[4][2] == 0 or matriz[4][2] > maior:
        maior = matriz[4][2]
    if matriz[5][2] == 0 or matriz[5][2] > maior:
        maior = matriz[5][2]
print('-' * 45)
print(f'[ {matriz[0][2]:^3} ] [ {matriz[1][2]:^3} ] [ {matriz[2][2]:^3} ]\n'
      f'[ {matriz[3][2]:^3} ] [ {matriz[4][2]:^3} ] [ {matriz[5][2]:^3} ]\n'
      f'[ {matriz[6][2]:^3} ] [ {matriz[7][2]:^3} ] [ {matriz[8][2]:^3} ]')
print('-' * 45)
print(f'A soma dos valores pares é {par}.')
print(f'A soma dos valores da terceira coluna é {matriz[2][2] + matriz[5][2] + matriz[8][2]}')
print(f'O maior número da segunda linha é {maior}.')
print('-' * 45)
