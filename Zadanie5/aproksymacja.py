import sympy as sp
from calkowanie import gauss_czybyszew


def wielomian_czybyszewa(stopien):
    x = sp.Symbol('x')
    lista = [sp.cos(i * sp.acos(x)) for i in range(2)]
    for i in range(2, stopien):
        lista.append(sp.simplify(2 * x * lista[i - 1] - lista[i - 2]))
    return lista


def aproksymacja(funkcja, stopien, wezly):
    x = sp.Symbol('x')
    T_k = wielomian_czybyszewa(stopien)
    wynik = sp.simplify(x - x)
    for i in range(stopien):
        temp = sp.simplify(funkcja * T_k[i])  # Ze wzoru wx * fx * Tx
        calka = gauss_czybyszew(temp, wezly) # całkujemy na warunek ortogonalnosci
        if i == 0:
            calka = calka / 3.141592653589793
        else:
            calka = calka / (3.141592653589793 / 2)
        # obliczamy wielomian aproksymacyjny zgodnie ze wzorem yx = c0g0(x) + ... + cmgm(x)
        wynik += sp.simplify(calka * T_k[i])
    return wynik
