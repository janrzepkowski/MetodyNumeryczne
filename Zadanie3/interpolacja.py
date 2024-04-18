from math import prod


def equidistant_nodes(a, b, n):
    """
        a: poczatek przedzialu
        b: koniec przedzialu
        n: liczba wezlow
        return: lista rownoodleglych wezlow
    """
    return [a + i * (b - a) / (n - 1) for i in range(n)]


def divided_differences(nodes_x, nodes_y):
    n = len(nodes_x)
    coef = nodes_y[:]
    for i in range(1, n):
        for j in range(n - 1, i - 1, -1):
            coef[j] = (coef[j] - coef[j - 1]) / (nodes_x[j] - nodes_x[j - i])
    return coef


def newton_interpolation(x, nodes_x, nodes_y):
    coef = divided_differences(nodes_x, nodes_y)
    n = len(nodes_x)
    return sum(coef[i] * prod(x - nodes_x[j] for j in range(i)) for i in range(n))


print(newton_interpolation(0.5, [-5, -1, 0, 2], [-2, 6, 1, 3]))
"""
    dziala obliczanie wartosci w punkcie dla interpolacji newtona
    sprawdzalem na tej stronce i ten sam wynik https://www.dcode.fr/newton-interpolating-polynomial
    nie wiem do konca jak to sie zgadza z poleceniem ale chyba solver to solver
"""