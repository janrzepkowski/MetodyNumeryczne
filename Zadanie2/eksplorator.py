import os


def display_files():
    files = [f for f in os.listdir() if os.path.isfile(f) and f.endswith('.txt')]
    if not files:
        print("Brak plików tekstowych w bieżącym katalogu.")
        return
    print("Dostępne pliki tekstowe:")
    for idx, file in enumerate(files, 1):
        print(f"{idx}. {file}")


def open_file(filename):
    while True:
        try:
            with open(filename, 'r') as file:
                print(f"Zawartość pliku '{filename}':")
                print(file.read())
            return filename  # Zwraca poprawną nazwę pliku
        except FileNotFoundError:
            print(f"Plik o nazwie '{filename}' nie istnieje.")
            filename = input("Podaj poprawną nazwę pliku: ")
