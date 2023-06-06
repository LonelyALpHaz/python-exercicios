#QUANTAS VEZES O NÚMERO 9 FOI DIGITADO
#EM QUE POSIÇÃO O NÚMERO 3 APARECE PELA 1ª VEZ
#QUAIS FORAM OS NÚMEROS PARES DIGITADOS
tres = 0
for c in range(0, 4):
    num = int(input('Digite um número: '))
    tupla = (num)
#NÚMERO 9 NA TUPLA:
for pos, tres in enumerate(tupla):
    print(pos)


