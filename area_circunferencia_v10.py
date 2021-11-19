#!/usr/bin/python3
import errno
from math import pi
import sys


def circulo(raio):
    return pi * float(raio) ** 2


def help():
    print("""\
            É necessário informar na frente do nome do arquivo o valor do raio""")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
        sys.exit(1)
        # ou
        # sys.exit(errno.EPERM)
    else:
        print(sys.argv[0])
        print(sys.argv[1])
        raio = sys.argv[1]
        area = circulo(raio)
        print(f'Área do círculo {area}')
