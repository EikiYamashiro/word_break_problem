#!/usr/bin/env python
# coding: utf-8
import time

def print_resultados(func, dic, entrada):
    print(" ")
    print("Para a Lista de Palavras: ", dic)
    print(" ")
    time.sleep(.5)

    saida = func(dic, entrada)
    time.sleep(.5)

    print(" ")
    print("A saída do programa é: ", saida)
    time.sleep(.5)

    print(" ")
    print("-------------------------//-------------------------")
    print(" ")
    time.sleep(.5)

def print_better(func, dic, entrada, lookup):
    print(" ")
    print("Para a Lista de Palavras: ", dic)
    print(" ")
    time.sleep(.5)

    saida = wordBreak_better(dic, entrada, lookup)
    time.sleep(.5)

    print(" ")
    print("A saída do programa é: ", saida)
    time.sleep(.5)

    print(" ")
    print("-------------------------//-------------------------")
    print(" ")
    time.sleep(.5)
