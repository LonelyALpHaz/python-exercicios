#MÉDIA, MAIOR E MENOR VALORE:
continuar = 'S'
media = soma = contador = menor = maior = 0
while continuar in 'Ss':
    num = int(input('Digite um valor: '))
    continuar = str(input('Quer continuar [S/N]? ').upper()).strip()[0]
    contador += 1
    soma += num
    numeros = [num]
    for num in numeros:
        if maior == 0 or num > maior:
            maior = num
        if menor == 0 or num < menor:
            menor = num
        media = soma / contador
    if continuar != 'S' and continuar != 'N':
        print('Comando inválido. utilize apenas "S" ou "N" na resposta.')
    if continuar == 'N':
        print('Você digitou {} números. A média é igual a {:.2f}.\nO maior número é {} e o menor número é {}.'.format(contador, media, maior, menor))
        break
