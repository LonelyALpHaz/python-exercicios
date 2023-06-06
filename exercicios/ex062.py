#PROGRESSÃO ARITIMÉTICA V3.0:
p1 = int(input('Primeiro termo da PA: '))
razao = int(input('Razão da PA: '))
d = p1 + (10 - 1) * razao
pa = p1
contador = 1
nadicional = 10
total = 0
while nadicional != 0:
    total = total + nadicional
    while contador <= total:
        print(pa, end=' -> ')
        pa += razao
        contador += 1
    print('PAUSA!')
    nadicional = int(input('\nQuantos termos a mais você deseja? '))
    if nadicional == 0:
        print('O total de termos adicionados é {}.'.format(contador - 1))
        break
print('Fim')
