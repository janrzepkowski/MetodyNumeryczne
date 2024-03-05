import numpy as np

def funkcja_wielomianowa(x):
    wspolczynniki = [0.25, 3, 2, 1]
    y = horner(wspolczynniki, x)
    return y

def funkcja_trygonometryczna(x):
    y = 4 * np.sin(x) - 2 * np.cos(x)
    return y

def funkcja_wykladnicza(x):
    y = 2 ** x - 4 ** x
    return y

def funkcja_zlozona(x):
    y = 2 * x ** 2 - np.cos(x) + 4**x

def horner(wspolczynniki, x):
    y = wspolczynniki[0]
    for i in range(1, len(wspolczynniki)):
        y = y * x + wspolczynniki[i]
    return y
