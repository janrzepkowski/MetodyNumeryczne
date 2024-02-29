
menu = """
Wybierz jedna z funkcji:
A - funkcja wielomianowa
B - funkcja trygonometryczna
C - funkcja wykladnicza
D - funkcja zlozona
"""

while True:
    print(menu)
    wybor = input("Wpisz A, B, C, D lub Q zeby zakonczyc: ")
    if wybor == "Q":
        break
