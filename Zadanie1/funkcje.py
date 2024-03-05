import numpy as np

def funkcja_wielomianowa(x):
    wspolczynniki = [1, 0, -60]
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
    return y

def horner(wspolczynniki, x):
    y = wspolczynniki[0]
    for i in range(1, len(wspolczynniki)):
        y = y * x + wspolczynniki[i]
    return y

def wartosc(wybor, x):
    y = 0
    if wybor == "1":
        y = funkcja_wielomianowa(x)
    elif wybor == "2":
        y = funkcja_trygonometryczna(x)
    elif wybor == "3":
        y = funkcja_wykladnicza(x)
    elif wybor == "4":
        y = funkcja_zlozona(x)
    return y