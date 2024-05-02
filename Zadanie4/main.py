from Zadanie4.funkcje import wartosc
from Zadanie4.metody import newton_cotes

def main():
    print("Wybierz funkcję do obliczenia:")
    print("0: wielomian wprowadzony ręcznie")
    print("1: wielomian predefiniowany")
    print("2: funkcja trygonometryczna")
    print("3: funkcja wykładnicza")
    print("4: funkcja liniowa")
    print("5: wartość absolutna")

    wybor = input("Twój wybór: ")
    a = float(input("Podaj początek przedziału: "))
    b = float(input("Podaj koniec przedziału: "))
    dokladnosc = float(input("Podaj dokładność: "))

    funkcja = lambda x: wartosc(wybor, x)
    wynik, ilosc_podprzedzialow = newton_cotes(funkcja, a, b, dokladnosc)

    print(f"Wynik: {wynik}, użyto {ilosc_podprzedzialow} podprzedziałów")

if __name__ == "__main__":
    main()