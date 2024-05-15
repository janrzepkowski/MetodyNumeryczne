import matplotlib.pyplot as plt
import numpy as np

from Zadanie4.funkcje import wartosc


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
        return "funkcja liniowa: f(x) = 2x-3"
    elif wybor_p == "5":
        return "funkcja bezwględna: |x-5|"


def plot_draw(wybor_p):
    x = np.linspace(0, 100, 100)
    plt.plot(x, wartosc(wybor_p, x), color='red', label='wykres funkcji')
    plt.grid()

    plt.title(plot_title(wybor_p))
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend(loc='lower right', framealpha=1, frameon=True)
    plt.tight_layout()
    plt.show()
