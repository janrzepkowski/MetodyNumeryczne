import numpy as np

is_input = False
coeffs = []


def linear(x):
    return 2 * x - 3


def absolute(x):
    return abs(x - 5)


def polynomial(x):
    coefficients = [1, 0, -60]
    return horner(coefficients, x)


def trigonometric(x):
    return 4 * np.sin(x) - 2 * np.cos(x)


def rational(x):
    return 2 * x ** 2 - np.cos(x) + 3


def horner(coefficients, x):
    y = coefficients[0]
    for i in range(1, len(coefficients)):
        y = y * x + coefficients[i]
    return y


def poly_by_hand(x):
    global is_input
    global coeffs
    if not is_input:
        is_input = True

        size = int(input("Wprowadz stopien wielomianu [1,...]: "))
        coeffs = list(range(size + 1))

        for i in range(size):
            coeffs[i] = float(input("Podaj wartość kolejnych współczynników: "))

        print(coeffs)

    return horner(coeffs, x)


functions = [
    # 0:
    ["wielomianowa", polynomial],
    # 1:
    ["liniowa", linear],
    # 2:
    ["|x - 5|", absolute],
    # 3:
    ["trygonometryczna", trigonometric],
    # 4:
    ["złożenie", rational],
    # 5:
    ["z ręki", poly_by_hand]
]


def print_function():
    for i in range(len(functions)):
        print(str(i) + ". " + functions[i][0])
    i = int(input("Wybierz funkcję: "))
    return functions[i][0], functions[i][1]
