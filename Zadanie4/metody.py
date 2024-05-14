import numpy as np
from Zadanie4.funkcje import wartosc


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

# def gauss_laguerre(function, nodes):
#     _sum = 0
#     _sum_values = 0
#     data = file.read_file()[nodes - 2]
#     for n in range(nodes):
#         wage = data[n][0]
#         x = data[n][1]
#         value = function(x)
#         _sum += wage * value
#         _sum_values += value
#         # print(wage, x, value)
#     # print(_sum_values)
#     return _sum
#
#
# # test
# from Zadanie4.funkcje import linear
# funkcja = lambda x: linear(x)
# for i in range(2, 50):
#     print(gauss_laguerre(funkcja, i))


def wspolczynniki(liczba_wezlow, numer_wezla):
    dane = (
            ((0.58578643762690, 0.85355339059327), (3.41421356237309, 0.14644660940672)),
            ((0.41577455678347, 0.71109300992917), (2.29428036027904, 0.27851773356924), (6.28994508293747, 0.01038925650158)),
            ((0.32254768961939, 0.60315410434163), (1.74576110115834, 0.35741869243779), (4.53662029692112, 0.03888790851500), (9.39507091230113, 0.00053929470556)),
            ((0.26356031971814, 0.52175561058280), (1.41340305910651, 0.39866681108317), (3.59642577104072, 0.07594244968170), (7.08581000585883, 0.00361175867992), (12.6408008442757, 0.00002336997238))
            )
    return dane[liczba_wezlow - 2][numer_wezla]


def gauss(wybor_funkcji, liczba_wezlow):
    wynik = 0
    for i in range(liczba_wezlow):
        x = (wspolczynniki(liczba_wezlow, i)[0])
        w = (wspolczynniki(liczba_wezlow, i)[1])
        wynik += w * wartosc(wybor_funkcji, x)
    return wynik