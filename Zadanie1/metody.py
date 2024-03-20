from funkcje import wartosc


def bisekcja(wybor, poczatek, koniec, iteracje, eps):
    x0 = 0

    if wartosc(wybor, poczatek) * wartosc(wybor, koniec) >= 0:
        return False

    else:
        if iteracje == 0:
            # d - osiągnięcie zadanej dokładności obliczeń
            n = 0
            while abs(koniec - poczatek) >= eps and n < 1000:
                x0 = (poczatek + koniec) / 2
                if wartosc(wybor, x0) == 0:
                    print("Korzystajac z metody bisekcji udalo sie znalezc rozwiazanie, "
                          "po " + str(n + 1) + " iteracjach")
                    return x0
                elif wartosc(wybor, x0) * wartosc(wybor, koniec) < 0:
                    poczatek = x0
                else:
                    koniec = x0
                n += 1
            print("Korzystajac z metody bisekcji udalo sie znaleźć przybliżone rozwiazanie, "
                  "po " + str(n) + " iteracjach")
            return x0

        else:
            # i - wykonanie określonej przez użytkownika liczby iteracji
            for n in range(iteracje):
                x0 = (poczatek + koniec) / 2
                if wartosc(wybor, x0) == 0:
                    print("Korzystajac z metody bisekcji udalo sie znalezc dokladne rozwiazanie (ε = 0), "
                          "po " + str(n + 1) + " iteracjach")
                    return x0
                if wartosc(wybor, x0) * wartosc(wybor, koniec) < 0:
                    poczatek = x0
                else:
                    koniec = x0

            # Oszacowanie dokladnosci wyniku: Wariant B: |f(xi)| < ε
            eps = abs(wartosc(wybor, x0))
            print("Korzystajac z metody bisekcji udalo sie znaleźć przybliżone rozwiazanie po " + str(iteracje) +
                  " iteracjach z dokladnoscia ε = " + str(eps))
            return x0


def sieczna_krok(wybor_p, poczatek_p, koniec_p):
    return koniec_p - (wartosc(wybor_p, koniec_p) * (koniec_p - poczatek_p)) / (
            wartosc(wybor_p, koniec_p) - wartosc(wybor_p, poczatek_p))


def siecznych(wybor, poczatek, koniec, iteracje, eps):
    x0 = 0

    if wartosc(wybor, poczatek) * wartosc(wybor, koniec) >= 0:
        return False

    else:
        if iteracje == 0:  # d - osiągnięcie zadanej dokładności obliczeń
            n = 0
            while abs(koniec - poczatek) >= eps and n < 1000:
                x0 = sieczna_krok(wybor, poczatek, koniec)

                if wartosc(wybor, x0) == 0:
                    print("Korzystajac z metody siecznych udalo sie znalezc dokladne rozwiazanie (ε = 0), po "
                          + str(n + 1) + " iteracjach")
                    return x0
                if wartosc(wybor, x0) * wartosc(wybor, koniec) < 0:
                    poczatek = x0
                else:
                    koniec = x0
                n += 1
            print("Korzystajac z metody siecznych udalo sie znaleźć przybliżone rozwiazanie po "
                  + str(n) + " iteracjach")
            return x0

        else:  # i - wykonanie określonej przez użytkownika liczby iteracji
            for n in range(iteracje):
                x0 = sieczna_krok(wybor, poczatek, koniec)

                if wartosc(wybor, x0) == 0:
                    print("Korzystajac z metody siecznych udalo sie znalezc dokladne rozwiazanie (ε = 0), po "
                          + str(n + 1) + " iteracjach")
                    return x0
                if wartosc(wybor, x0) * wartosc(wybor, koniec) < 0:
                    poczatek = x0
                else:
                    koniec = x0
            eps = abs(wartosc(wybor, x0))  # Oszacowanie dokladnosci wyniku: Wariant B: |f(xi)| < ε
            print("Korzystajac z metody siecznych udalo sie znaleźć przybliżone rozwiazanie po " + str(iteracje) +
                  " iteracjach z dokladnoscia ε = " + str(eps))
            return x0
