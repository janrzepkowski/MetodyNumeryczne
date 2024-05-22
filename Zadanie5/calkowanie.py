from numpy.polynomial.chebyshev import chebgauss
import sympy as sp


def wspolczynniki(wezly):
    A_i, x_i = chebgauss(wezly)
    return A_i, x_i


def gauss_czybyszew(wybor, wezly):
    x = sp.Symbol('x')
    A_i, x_i = wspolczynniki(wezly)
    wynik = sp.simplify(x - x)
    for i in range(wezly):
        wynik += x_i[i] * wybor.subs(x, A_i[i])
    return wynik
