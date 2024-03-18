import pylab as pl

from metody import bisekcja, siecznych
from funkcje import wartosc
import numpy as np
from matplotlib import pyplot as plt

menu = """
Wybierz jedną z funkcji:
    0 - funkcja wielomianowa "z ręki"
    1 - funkcja wielomianowa
    2 - funkcja trygonometryczna
    3 - funkcja wykładnicza
    4 - funkcja złożona
    5 - wyjście
"""
poczatek = 0
koniec = 0
kryterium = ""
kryt = """
Wybierz kryterium stopu algorytmu:
    d - osiągnięcie zadanej dokładności obliczeń
    i - wykonanie określonej przez użytkownika liczby iteracji
"""
iteracje = 0
eps = 0


def plot_title(wybor_p):
    if wybor_p == "0":
        return "funkcja wielomianowa z ręki"
    elif wybor_p == "1":
        return "funkcja wielomianowa: f(x) = x^2 - 60"
    elif wybor_p == "2":
        return "funkcja trygonometryczna: f(x) = 4*sinx - 2*cosx"
    elif wybor_p == "3":
        return "funkcja wykładnicza: f(x) = 2^x - 4^x"
    elif wybor_p == "4":
        return "funkcja złożona: f(x) = 2*x^2 - cos(x) + 4^x"


def plot_draw(wybor_p, bis_p, sie_p):
    x = np.linspace(poczatek, koniec, 100)

    plt.plot(x, wartosc(wybor_p, x), color='red', label='wykres funkcji')
    plt.plot(sie_p, wartosc(wybor_p, sie_p), color='green', marker='o', label='met. siecznych')
    plt.plot(bis_p, wartosc(wybor_p, bis_p), markeredgecolor='blue', markerfacecolor='none', marker='o', label='met. bisekcji')
    plt.grid()

    pl.title(plot_title(wybor_p))
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend(loc='lower right', framealpha=1, frameon=True)
    plt.tight_layout()
    plt.show()


while True:
    print(menu)
    wybor = input("Wpisz 0, 1, 2, 3, 4 lub 5 żeby zakończyć: ")

    if wybor == "5":
        break

    elif wybor in "01234":
        while True:
            try:
                poczatek = float(input("Wprowadz wartosc poczatku przedzialu: "))
                break
            except ValueError:
                print("Wartosci musza byc liczbami")

        while True:
            try:
                koniec = float(input("Wprowadz wartosc konca przedzialu: "))
                break
            except ValueError:
                print("Wartosc musi byc liczba")

        while True:
            kryterium = input(kryt)
            if kryterium in "di":
                break
            else:
                print("Wpisz d lub i")

        if kryterium == "i":
            while True:
                try:
                    iteracje = abs(int(input("Wprowadz liczbe iteracji: ")))
                    eps = 0
                    break
                except ValueError:
                    print("Liczba iteracji musi byc dodatnia i calkowita")

        elif kryterium == "d":
            while True:
                try:
                    eps = abs(float(input("Wprowadz wartosc dokladnosci: ")))
                    iteracje = 0
                    break
                except ValueError:
                    print("Wartosc dokladnosci musi byc liczba")

        bis = bisekcja(wybor, poczatek, koniec, iteracje, eps)
        print("Wartość x0 znalezniona przy użyciu metod bisekcji: " + str(bis))
        sie = siecznych(wybor, poczatek, koniec, iteracje, eps)
        print("Wartość x0 znalezniona przy użyciu metod siecznych: " + str(sie))

        plot_draw(wybor, bis, sie)

        if not bis or not sie:
            print("Funkcja nie spelnia podstawowego warunku: f(a)f(b) < 0")

    else:
        print("Wybrano nieprawidlowa wartosc")
