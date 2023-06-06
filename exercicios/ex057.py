#MASCULINO E FEMININO:
masculino = 'M'
feminino = 'F'
while masculino == masculino and feminino == feminino:
    sexo = str(input('Sexo [M/F]: ')).upper()
    if sexo != masculino and sexo != feminino:
        print('Comando inválido. Utilize apenas "M" ou "F".')
        break
