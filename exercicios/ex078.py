#MAIOR E MENOR VALOR EM LISTAS:
maior = menor = 0
valores = list()
for cont in range(0, 5):
    valores.append(int(input(f'Diggite um valor para a posição {cont}: ')))
    maior = max(valores)
    menor = min(valores)
for p, c in enumerate(valores):
    print(f'Você digitou os valores: {valores}')
    print(f'O maior valor digitado foi {maior} nas posições {valores.index(maior)}.')
    print(f'O menor valor digitado foi {menor} nas posições {valores.index(menor)}.')
    break
