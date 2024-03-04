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
i - wykonanie określonej przez użytkownika liczby iteracji.
"""
iteracje = 0
dokladnosc = 0

while True:
    print(menu)
    funkcja = input("Wpisz 1, 2, 3, 4 lub 5 żeby zakończyć: ")
    if funkcja == "5":
        break
    elif funkcja in "1234":
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
                    dokladnosc = 0
                    break
                except ValueError:
                    print("Liczba iteracji musi byc dodatnia i calkowita")

        elif kryterium == "d":
            while True:
                try:
                    dokladnosc = abs(float(input("Wprowadz wartosc dokladnosci: ")))
                    iteracje = 0
                    break
                except ValueError:
                    print("Wartosc dokladnosci musi byc liczba")

