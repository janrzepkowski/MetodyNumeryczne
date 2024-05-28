from sympy import symbols

from Zadanie5.aproksymacja import aproksymacja, wykresy
from Zadanie5.funkcje import wartosc


def main():
    print("Wybierz aproksymowaną funkcję:")
    print("1. Funkcja liniowa: 2x - 3")
    print("2. Funkcja bezwzględna: |x - 5|")
    print("3. Wielomian predefiniowany: x^2 - 60")
    print("4. Wielomian wprowadzony ręcznie")
    print("5. Funkcja trygonometryczna: 4sin(x) - 2cos(x)")
    print("6. Złożenie funkcji: 2x - cos(x) + 3")

    wybor = input("Twój wybór: ")
    x = symbols('x')
    funkcja = wartosc(wybor, x)
    a = float(input("Wprowadź początek przedziału aproksymacji: "))
    b = float(input("Wprowadź koniec przedziału aproksymacji: "))
    tryb = input("Wybierz tryb pracy: \n1. Program dobiera stopień wielomianu\n2. Wprowadź stopień wielomianu: ")

    if tryb == "1":
        epsilon = float(input("Wprowadź oczekiwany błąd aproksymacji: "))

    if tryb == "2":
        stopien = int(input("Wprowadź stopień wielomianu aproksymującego: "))
        wezly = int(input("Wprowadź ilość węzłów: "))

        wynik = aproksymacja(funkcja, stopien + 1, wezly)
        print("Wielomian aproksymujący: ", wynik)

        wykresy(a, b, funkcja, stopien + 1, wezly)

if __name__ == "__main__":
    main()
