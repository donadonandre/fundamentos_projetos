#!/usr/bin/python3
from math import pi
import sys


def circulo(raio):
    return pi * float(raio) ** 2


if __name__ == '__main__':
    print(sys.argv[0])
    print(sys.argv[1])
    raio = sys.argv[1]
    area = circulo(raio)
    print(f'Área do círculo {area}')
