#FUNÇÃO QUE DIZ O MAIOR NÚMERO:
from time import sleep


def maior(* num):
    print('-' * (40 + len(num) + 2))
    print('Recebi os seguintes valores:', end=' ')
    for v in num:
        print(f'\033[1;34m{v}\033[m', end=' ')
        sleep(0.5)
    print()
    print(f'\033[1;34mAo todo foram \033[1;33m{len(num)}\033[m\033[1;34m valor(es). '
          f'O maior valor é \033[1;33m{max(num)}\033[m.\033[m')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
