import numpy as np
from sympy import *
from matplotlib import pyplot as plt

from calkowanie import gauss_czebyszew


def wielomian_czybyszewa(stopien):
    x = Symbol('x')
    lista = [cos(i * acos(x)) for i in range(2)]
    for i in range(2, stopien):
        lista.append(simplify(2 * x * lista[i - 1] - lista[i - 2]))
    return lista


def aproksymacja(funkcja, stopien, wezly):
    x = Symbol('x')
    T_k = wielomian_czybyszewa(stopien)
    wynik = simplify(x - x)
    for i in range(stopien):
        temp = simplify(funkcja * T_k[i])  # Ze wzoru wx * fx * Tx
        calka = gauss_czebyszew(temp, wezly)  # całkujemy na warunek ortogonalnosci
        if i == 0:
            calka = calka / 3.141592653589793
        else:
            calka = calka / (3.141592653589793 / 2)
        # obliczamy wielomian aproksymacyjny zgodnie ze wzorem yx = c0g0(x) + ... + cmgm(x)
        wynik += simplify(calka * T_k[i])
    return wynik


def blad(a, b, funkcja, stopien, wezly):
    x = Symbol('x')
    y_x = aproksymacja(funkcja, stopien, wezly)
    suma = simplify(x - x)
    punkty = np.linspace(a, b, stopien)
    for p in punkty:
        suma += (funkcja.subs(x, p) - y_x.subs(x, p)) ** 2
    wynik = simplify(sqrt(suma))
    return wynik / 100


def wykresy(a, b, funkcja, stopien, wezly):
    x = Symbol('x')
    apro = aproksymacja(funkcja, stopien, wezly)
    x_apro = np.linspace(a, b, 100)
    y_apro = [apro.subs(x, i) for i in x_apro]
    y_real = [funkcja.subs(x, i) for i in x_apro]
    plt.figure(figsize=(10, 7))
    plt.plot(x_apro, y_apro)
    plt.plot(x_apro, y_real, "r", linestyle='--')
    plt.xlabel("Oś OX")
    plt.ylabel("Oś OY")
    plt.axhline(y=0, color='black', linestyle='-')
    plt.axvline(x=0, color='black', linestyle='-')
    plt.show()