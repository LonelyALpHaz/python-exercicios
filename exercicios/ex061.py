#PROGRESSÃO ARITIMÉTICA V2.0:
p1 = int(input('Primeiro termo da PA: '))
r = int(input('Razão da PA: '))
d = p1 + (10 - 1) * r
pa = p1
count = 0
while count < 10:
    print(pa, end=' -> ')
    pa += r
    count += 1
print('ACABOU!')
