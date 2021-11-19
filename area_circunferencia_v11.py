#!/usr/bin/python3
import errno
from math import pi
import sys


class TerminalColor:
    ERRO = '\033[91m'
    NORMAL = '\033[0m'

def circulo(raio):
    return pi * float(raio) ** 2


def help():
    print("""\
            É necessário informar na frente do nome do arquivo o valor do raio""")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
        sys.exit(errno.EPERM)

    if not sys.argv[1].isnumeric():
        help()
        print(TerminalColor.ERRO + 'Você não passou um argumento válido' + TerminalColor.NORMAL)
        sys.exit(errno.EINVAL)


    print(sys.argv[0])
    print(sys.argv[1])
    raio = sys.argv[1]
    area = circulo(raio)
    print(f'Área do círculo {area}')
