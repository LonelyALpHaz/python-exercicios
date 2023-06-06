#DETECTOR DE POLÍNDROMOS:
frase = str(input('Digite uma frase: ').strip()).upper()
n = frase.replace(' ', '')
m = frase[::-1].replace(' ', '').upper()
print('A frase digitada foi {} e essa frase ao contrário é {}. Logo...'.format(frase, m))
if n == m:
    print('A frase É um palínromo.')
else:
    print('A frase NÃO É um palíndromo.')
