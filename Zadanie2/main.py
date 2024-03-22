from eksplorator import display_files, open_file

eps = 0
iter = 0

while True:
    print("\nMenu:")
    print("1. Wyświetl dostępne pliki tekstowe")
    print("2. Otwórz plik z którego zostanie wczytany układ równań")
    print("3. Zakończ działanie programu")

    choice = input("\nWybierz opcję: ")

    if choice == '1':
        display_files()
    elif choice == '2':
        filename = input("Podaj nazwę pliku do otwarcia: ")
        filename = open_file(filename)  # Przypisanie poprawnej nazwy pliku zwróconej przez funkcję open_file

        while True:
            N = input("Podaj z ilu równań ma składać się układ: ")
            try:
                N = int(N)  # Konwersja na liczbę całkowitą
                with open(filename, 'r') as data:
                    lines = data.readlines()
                    if len(lines) < N:
                        print("Nieprawidłowa wartość. Wprowadź liczbę nie większą niż liczba równań w układzie.")
                    else:
                        break
            except ValueError:
                print("Nieprawidłowa wartość. Podaj liczbę całkowitą.")

        matrix = []
        vector = []

        with open(filename, 'r') as data:
            for line in lines[:N]:
                coefficients = list(map(int, line.split()))  # Dzieli linię i konwertuje na liczby całkowite
                matrix.append(coefficients[:-1])  # Dodaje współczynniki do macierzy (bez ostatniego elementu)
                vector.append(coefficients[-1])  # Dodaje ostatni element jako element wektora

        print("Macierz współczynników:")
        for row in matrix:
            print(row)

        print("Wektor wyrazów wolnych:")
        print(vector)

    elif choice == '3':
        break
    else:
        print("Nieprawidłowa opcja. Wybierz ponownie spośród 1, 2 lub 3")
