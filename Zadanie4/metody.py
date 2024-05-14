from Zadanie4.funkcje import wartosc
import numpy as np


def metoda_simpsona(a, b, funkcja):
    h = (b - a) / 2
    calka = (np.exp(-a) * wartosc(funkcja, a)
             + 4 * np.exp(-(a + b) / 2) * wartosc(funkcja, ((a + b) / 2))
             + np.exp(-b) * wartosc(funkcja, b)) * h / 3
    return calka


def zlozona_metoda_simpsona(poczatek, koniec, funkcja, dokladnosc):
    calka = metoda_simpsona(poczatek, koniec, funkcja)
    warunek = True
    n = 2
    while warunek:
        nowa_calka = 0
        h = (koniec - poczatek) / (2 * n)
        a = poczatek
        b = a + 2 * h
        for i in range(n):
            i = metoda_simpsona(a, b, funkcja)
            nowa_calka += i
            a = b
            b += 2 * h
        if abs(nowa_calka - calka) < dokladnosc:
            warunek = False
            calka = nowa_calka
        else:
            calka = nowa_calka
            n += 1
    return calka


def newton_cotes(funkcja, dokladnosc):
    a = 0
    delta = 1
    suma = 0
    flag = True
    while flag:
        calka = zlozona_metoda_simpsona(a, a + delta, funkcja, dokladnosc)
        suma += calka
        a += delta
        if abs(calka) <= abs(dokladnosc):
            flag = False
    return suma


def wspolczynniki(liczba_wezlow, numer_wezla):
    dane = (
            ((0.58578643762690, 0.85355339059327), (3.41421356237309, 0.14644660940672)),
            ((0.41577455678347, 0.71109300992917), (2.29428036027904, 0.27851773356924),
             (6.28994508293747, 0.01038925650158)),
            ((0.32254768961939, 0.60315410434163), (1.74576110115834, 0.35741869243779),
             (4.53662029692112, 0.03888790851500), (9.39507091230113, 0.00053929470556)),
            ((0.26356031971814, 0.52175561058280), (1.41340305910651, 0.39866681108317),
             (3.59642577104072, 0.07594244968170), (7.08581000585883, 0.00361175867992),
             (12.6408008442757, 0.00002336997238))
            )
    return dane[liczba_wezlow - 2][numer_wezla]


def gauss(funkcja, liczba_wezlow):
    wynik = 0
    for i in range(liczba_wezlow):
        x = (wspolczynniki(liczba_wezlow, i)[0])
        w = (wspolczynniki(liczba_wezlow, i)[1])
        wynik += w * wartosc(funkcja, x)
    return wynik
