#SEQUÊNCIA DE FIBONACCI V1.0:
num = int(input('Quantos termos você deseja ver? '))
proximo = 1
anterior = 1
contador = 0
while contador < num:
    print(0 + proximo, end=' -> ')
    contador += 1
    proximo = anterior + proximo
    anterior = proximo - anterior
print('ACABOU!')
