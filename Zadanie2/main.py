from gauss_jordan import find_solution, print_m
from eksplorator import display_files, open_file

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

        with open(filename, 'r') as data:
            for line in lines[:N]:
                coefficients = list(map(float, line.split()))  # Dzieli linię i konwertuje na liczby zmiennoprzecinkowe
                matrix.append(coefficients)  # Dodaje całą linię do macierzy

        solution = find_solution(matrix)

    elif choice == '3':
        break
    else:
        print("Nieprawidłowa opcja. Wybierz ponownie spośród 1, 2 lub 3")
