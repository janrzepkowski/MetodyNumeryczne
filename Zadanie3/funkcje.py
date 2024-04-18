import numpy as np


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


def value(choice, x):
    if choice == "1":
        return linear(x)
    elif choice == "2":
        return absolute(x)
    elif choice == "3":
        return polynomial(x)
    elif choice == "4":
        return trigonometric(x)
    elif choice == "5":
        return rational(x)
    return 0
