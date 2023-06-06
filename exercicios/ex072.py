#NÚMERO POR EXTENSO:
numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
           'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze',
           'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    resposta = int(input('Digite um número entre 0 e 20: '))
    while resposta not in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20):
        resposta = int(input('Número inválido. Digite um número entre 0 e 20: '))
    print(f'Você digitou o número {numeros[resposta]}.')
    break
