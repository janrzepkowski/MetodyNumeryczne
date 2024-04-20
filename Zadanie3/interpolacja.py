import numpy as np


def equidistant_nodes(a, b, n):
    return np.linspace(a, b, n)


def interpolation_coefficients(node_x, node_y):
    n = len(node_y)
    h = abs(node_x[1] - node_x[0])
    pascal_triangle = np.zeros([n, n])
    pascal_triangle[:, 0] = 1
    np.fill_diagonal(pascal_triangle, 1)

    for i in range(2, n):
        for j in range(1, i + 1):
            pascal_triangle[i][j] = pascal_triangle[i - 1][j - 1] + pascal_triangle[i - 1][j]

    coef = [node_y[0]]
    strong = 1
    for k in range(1, n):
        total = 0
        for i in range(k + 1):
            tmp = node_y[i] * pascal_triangle[k][i]
            if (k - i) % 2 == 1: tmp *= -1
            total += tmp
        coef.append(total / strong)
        strong *= k + 1

    return coef, h


def interpolation_value(node_x, coef, h, x):
    result = 0
    t = (x - node_x[0]) / h
    for i in range(len(node_x)):
        tmp = coef[i]
        for j in range(i):
            tmp *= t - j
        result += tmp

    return result
