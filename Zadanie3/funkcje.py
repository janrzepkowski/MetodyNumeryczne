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


'''
0. wielomianowa (horner)
1. liniowa
2. |x|
3. trygonometryczna
4. złożenie
'''

functions = [
    # 0:
    ["wielomianowa", polynomial],
    # 1:
    ["liniowa", linear],
    # 2:
    ["|x|", absolute],
    # 3:
    ["trygonometryczna", trigonometric],
    # 4:
    ["złożenie", rational],
]


def print_function():
    for i in range(len(functions)):
        print(str(i) + ". " + functions[i][0])
    i = int(input("Wybierz funkcję: "))
    return functions[i][0], functions[i][1]
