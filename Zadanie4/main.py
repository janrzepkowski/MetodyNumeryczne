from Zadanie4.metody import newton_cotes, gauss


def main():
    print("Wybierz funkcję do obliczenia:")
    print("0. Wielomian wprowadzony ręcznie")
    print("1. Wielomian predefiniowany: x^2 - 60")
    print("2. Funkcja trygonometryczna: 4sin(x) - 2cos(x)")
    print("3. Funkcja wykładnicza: 2^x - 4^x")
    print("4. Funkcja liniowa: 2x - 3")
    print("5. Funkcja bezwzględna: |x - 5|")

    wybor = input("Twój wybór: ")
    dokladnosc = float(input("Podaj dokładność: "))

    wynik_newton = newton_cotes(wybor, dokladnosc)  # Używamy funkcji newton_cotes

    print(f"Wynik dla Newtona-Cotesa: {wynik_newton}")

    liczba_wezlow = int(input("Podaj liczbę węzłów dla metody Gaussa-Laguerre: "))
    wynik_gauss = gauss(wybor, liczba_wezlow)

    print(f"Wynik dla metody Gaussa-Laguerre: {wynik_gauss}, użyto {liczba_wezlow} węzłów")


def research():
    for fun in range(1, 6):
        if fun == 3:
            continue
        fun = str(fun)
        print(f"FUNKCJA: {fun}")
        wynik_newton = newton_cotes(fun, 0.001)
        print(f"Wynik newton: {wynik_newton}")
        for liczba_wezlow in range(2, 6):
            wynik_gauss = gauss(fun, liczba_wezlow)
            print(f"Wynik gauss: {wynik_gauss} dla {liczba_wezlow} wezlow")
            blad = abs(wynik_newton - wynik_gauss)
            print(f"Blad: {blad}")
        print("-------------------")


def choose():
    print("Wybierz ")
    print("1. research")
    print("2. testowanie przypadku")

    choice = input("Wybór: ")

    match choice:
        case "1":
            research()
        case "2":
            main()
        case _:
            print("choose correct option")
            choose()


if __name__ == "__main__":
    choose()
