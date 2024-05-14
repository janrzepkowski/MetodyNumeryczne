import numpy as np
import file


def oblicz_wartosci(funkcja, a, b, ilosc_podprzedzialow):
    h = (b - a) / ilosc_podprzedzialow
    x = np.linspace(a, b, ilosc_podprzedzialow + 1)
    wartosci = funkcja(x)
    return wartosci, h


def oblicz_kwadrature(wartosci, h):
    wynik = wartosci[0] + wartosci[-1] + 4 * np.sum(wartosci[1:-1:2]) + 2 * np.sum(wartosci[2:-1:2])
    wynik *= h / 3
    return wynik


def newton_cotes(funkcja, a, b, dokladnosc):
    ilosc_podprzedzialow = 2
    stary_wynik = 0
    while True:
        wartosci, h = oblicz_wartosci(funkcja, a, b, ilosc_podprzedzialow)
        wynik = oblicz_kwadrature(wartosci, h)
        if abs(stary_wynik - wynik) < dokladnosc:
            return wynik, ilosc_podprzedzialow
        ilosc_podprzedzialow *= 2
        stary_wynik = wynik


# całkowanie metodą kwadratury gaussa:
# przedział: [0,+∞)
# waga: e^-x z pliku dla x

def gauss_laguerre(function, nodes):
    _sum = 0
    _sum_values = 0
    data = file.read_file()[nodes - 2]
    for n in range(nodes):
        wage = data[n][0]
        x = data[n][1]
        value = function(x)
        _sum += wage * value
        _sum_values += value
        # print(wage, x, value)
    # print(_sum_values)
    return _sum


# test
from Zadanie4.funkcje import linear
funkcja = lambda x: linear(x)
for i in range(2, 50):
    print(gauss_laguerre(funkcja, i))
