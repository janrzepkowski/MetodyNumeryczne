import numpy as np


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
