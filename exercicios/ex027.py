#PRIMEIRO E ÚLTIMO NOME:
n = str(input('Digite seu nome: ').strip()).split()
p = len(n) - 1
print('Muito prazer em te conhecer!\nO seu primeiro nome é {}\nO seu último nome é {}'.format(n[0], n[p]))
