# -*- coding: utf-8 -*-
__author__ = 'infante'

u"""Módulo para comparação de performance para algumas operações com strings em python"""

import time
from collections import OrderedDict


def comparacao_de_concatenacao():
    resultados = OrderedDict({1: None, 2: None, 3: None})
    nums = ""
    inicio = time.time()
    for n in range(1000000):
        nums += str(n)
    fim = time.time()
    resultados[1] = fim - inicio

    nums = []
    inicio = time.time()
    for n in range(1000000):
        nums.append(str(n))
    ''.join(nums)
    fim = time.time()
    resultados[2] = fim - inicio

    inicio = time.time()
    ''.join([str(num) for num in range(1000000)])
    fim = time.time()
    resultados[3] = fim - inicio

    for key in resultados.keys():
        print u"Método {0}: {1}s".format(key, resultados[key])


if __name__ == "__main__":
    comparacao_de_concatenacao()
