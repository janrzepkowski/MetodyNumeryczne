import numpy as np

is_input = False
coeffs = []


def poly_by_hand(x):
    global is_input
    global coeffs
    if not is_input:
        is_input = True

        size = int(input("Wprowadz stopien wielomianu [0,1,...]: "))
        coeffs = list(range(size))

        for i in range(size):
            coeffs[i] = float(input("Podaj wartości kolejnych współczynników: "))

        print(coeffs)

    return horner(coeffs, x)


def absolute(x):
    return abs(x - 5)


def linear(x):
    return 2 * x - 3


def polynomial(x):
    coefficients = [1, 0, -60]
    return horner(coefficients, x)


def trigonometric(x):
    return 4 * np.sin(x) - 2 * np.cos(x)


def exponential(x):
    return 2 ** x - 4 ** x


def horner(coefficients, x):
    y = coefficients[0]
    for i in range(1, len(coefficients)):
        y = y * x + coefficients[i]
    return y


def wartosc(wybor, x):
    match wybor:
        case "0":
            return poly_by_hand(x)
        case "1":
            return polynomial(x)
        case "2":
            return trigonometric(x)
        case "3":
            return exponential(x)
        case "4":
            return linear(x)
        case "5":
            return absolute(x)
        case _:
            return 0
