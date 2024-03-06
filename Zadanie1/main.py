from metody import bisekcja, siecznych

menu = """
Wybierz jedną z funkcji:
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

while True:
    print(menu)
    wybor = input("Wpisz 1, 2, 3, 4 lub 5 żeby zakończyć: ")
    if wybor == "5":
        break
    elif wybor in "1234":
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
        sie = siecznych(wybor, poczatek, koniec, iteracje, eps)

        if bis == False:
            print("Funkcja nie spelnia podstawowego warunku: f(a)f(b) < 0")
    else:
        print("Wybrano nieprawidlowa wartosc")