lst = ['CeV', 'CURSO EM VÍDEO', 'CURSO DE PYTHON', 'DESENVOLVEDOR PYTHON']
for pos, x in enumerate(lst):
    def escreva():
        tam = len(lst[pos])
        print('-' * (tam + 2))
        print(f' {lst[pos]}')
        print('-' * (tam + 2))
    escreva()
