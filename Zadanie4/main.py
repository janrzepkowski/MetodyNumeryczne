from Zadanie4.funkcje import wartosc
from Zadanie4.metody import newton_cotes
from Zadanie4.metody import gauss as gauss


def main():
    print("Wybierz funkcję do obliczenia:")
    print("0. Wielomian wprowadzony ręcznie")
    print("1. Wielomian predefiniowany: x^2 - 60")
    print("2. Funkcja trygonometryczna: 4sin(x) - 2cos(x)")
    print("3. Funkcja wykładnicza: 2^x - 4^x")
    print("4. Funkcja liniowa: 2x - 3")
    print("5. Funkcja bezwzględna: |x - 5|")

    wybor = input("Twój wybór: ")
    a = float(input("Podaj początek przedziału: "))
    b = float(input("Podaj koniec przedziału: "))
    dokladnosc = float(input("Podaj dokładność: "))

    funkcja = lambda x: wartosc(wybor, x)
    wynik, ilosc_podprzedzialow = newton_cotes(funkcja, a, b, dokladnosc)

    print(f"Wynik dla Newtona-Cotesa: {wynik}, użyto {ilosc_podprzedzialow} podprzedziałów")

    liczba_wezlow = int(input("Podaj liczbę węzłów dla metody Gaussa-Laguerre: "))
    wynik_gauss = gauss(wybor, liczba_wezlow)

    print(f"Wynik dla metody Gaussa-Laguerre: {wynik_gauss}, użyto {liczba_wezlow} węzłów")


if __name__ == "__main__":
    main()
