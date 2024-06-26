from sympy import symbols

from Zadanie5.aproksymacja import aproksymacja, wykresy, blad, auto_adapt
from Zadanie5.funkcje import wartosc


def main():
    print("Wybierz aproksymowaną funkcję:")
    print("1. Funkcja liniowa: 2x - 3")
    print("2. Funkcja bezwzględna: |x|")
    print("3. Wielomian predefiniowany: x^2 - 60")
    print("4. Wielomian wprowadzony ręcznie")
    print("5. Funkcja trygonometryczna: sin(x)")
    print("6. Złożenie funkcji: 2x - cos(x) + 3")

    wybor = input("Twój wybór: ")
    x = symbols('x')
    funkcja = wartosc(wybor, x)
    a = float(input("Wprowadź początek przedziału aproksymacji: "))
    b = float(input("Wprowadź koniec przedziału aproksymacji: "))
    tryb = input(
        "Wybierz tryb pracy: \n"
        "1. Program dobiera stopień wielomianu\n"
        "2. Wprowadź stopień wielomianu: ")

    if tryb == "1":
        wezly = int(input("Wprowadź ilość węzłów: "))
        epsilon = float(input("Wprowadź oczekiwany błąd aproksymacji: "))

        stopien, wynik = auto_adapt(a, b, funkcja, wezly, 2, epsilon)
        print("Wielomian aproksymujący: ", wynik)
        bld = blad(a, b, funkcja, stopien, wezly)
        print("Błąd aproksymacji: ", bld)

    if tryb == "2":
        stopien = 1 + int(input("Wprowadź stopień wielomianu aproksymującego: "))
        wezly = int(input("Wprowadź ilość węzłów: "))

        wynik = aproksymacja(funkcja, stopien, wezly)
        print("Wielomian aproksymujący: ", wynik)
        bld = blad(a, b, funkcja, stopien, wezly)
        print("Błąd aproksymacji: ", bld)

    wykresy(a, b, funkcja, stopien, wezly)


if __name__ == "__main__":
    main()

# 1. wybierz funkcje
# 2. przedział aproksymacji
# 3. stopień wielomianu aproksymującego
# 4. parametry związane z całkowaniem (np. il. węzłów) -> wykorzystać laguerre
# 5. wyznacz wielomian aproksymacyjny  danego stopnia
# 6. wykres wielomianu oraz oryginalny
# 7. oblicz błąd aproksymacji
# ---- na 5 ----
# 8. oczekiwany błąd aproksymacji
# 9. program iteracyjnie dobiera stopień wielomianu aproksymacyjnego
