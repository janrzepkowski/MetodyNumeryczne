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
            coeffs[i] = float(input("Podaj wartość kolejnych współczynników: "))

        print(coeffs)

    return horner(coeffs, x)


def polynomial(x):
    coefficients = [1, 0, -60]
    y = horner(coefficients, x)
    return y


def trigonometric(x):
    y = 4 * np.sin(x) - 2 * np.cos(x)
    return y


def exponential(x):
    y = 2 ** x - 4 ** x
    return y


def rational(x):
    y = 2 * x ** 2 - np.cos(x) + 4 ** x
    return y


def horner(coefficients, x):
    y = coefficients[0]
    for i in range(1, len(coefficients)):
        y = y * x + coefficients[i]
    return y


def wartosc(wybor, x):
    y = 0
    if wybor == "0":
        y = poly_by_hand(x)
    elif wybor == "1":
        y = polynomial(x)
    elif wybor == "2":
        y = trigonometric(x)
    elif wybor == "3":
        y = exponential(x)
    elif wybor == "4":
        y = rational(x)
    return y
