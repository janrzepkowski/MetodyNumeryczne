from numpy.linalg import matrix_rank
import numpy as np


# NOTES:
# 3 stany układu równań:
#  - oznaczony
#  - nieoznaczony
#  - sprzeczny

# do określenia z czym mamy do czynienia -> współczynnik macierzy

# https://www.matmana6.pl/twierdzenie-kroneckera-capellego
# rząd A = columnLength
#
# detA = 0 -> sprzeczny
# detA != 0 -> oznaczony


# tworzy format A|I|b
def attach_unit_matrix(matrix):
    column_length = len(matrix)

    index = 0
    for i in matrix:
        for j in range(column_length):
            if index == j:
                i.insert(j + column_length, 1)
            else:
                i.insert(j + column_length, 0)

        index += 1

    return matrix


# wyświetla matrix 2D
# wyświetla matrix 2D
def print_m(matrix):
    for i in matrix:
        rounded_row = [round(num, 4) for num in i]
        print(rounded_row)
    print()


# właściwa metoda rozwiania A|I|b -> I|A^-1|X, gdzie X - rozwiązania
def gauss_jordan(matrix):
    column_length = len(matrix)
    row_length = len(matrix[0])

    for i in range(column_length):
        # Jeśli na przekątnej jest 0, zamień wiersze
        if matrix[i][i] == 0:
            for j in range(i+1, column_length):
                if matrix[j][i] != 0:
                    matrix[i], matrix[j] = matrix[j], matrix[i]
                    break
            else:
                continue

        # Jeśli na przekątnej nie ma 1, to dzieli wiersz przez tę liczbę
        i_value = matrix[i][i]
        for j in range(row_length):
            matrix[i][j] /= i_value

        # Jeśli kolumna nie jest postaci jednostkowej to:
        for k in range(column_length):
            if k != i:
                # znajduje wartość w kolejnym wierszu
                coeff_to_zero = matrix[k][i]

                # każde pole w danym wierszu jest pomniejszone o (wartość coeff) * (wartość z kolumny wyżej)
                for j in range(2 * column_length + 1):
                    matrix[k][j] -= coeff_to_zero * matrix[i][j]

    return matrix


# wyciąga rozwiązania z I|A^-1|X
def get_solution(matrix):
    solution = []
    row_length = len(matrix[0])

    for i in matrix:
        solution.append(round(i[row_length - 1], 1))  # Zaokrąglenie do liczby z jednym miejscem po przecinku

    return solution


# funkcja do wywołania
def find_solution(matrix):
    system_type = check_system(matrix)
    if system_type == 'oznaczony':
        matrix_unit_solution = attach_unit_matrix(matrix)
        print_m(matrix_unit_solution)

        solved = gauss_jordan(matrix_unit_solution)
        print_m(solved)

        solution = get_solution(solved)
        print("Układ jest oznaczony. Rozwiązaniem są liczby:", solution)
        return solution
    else:
        print(f"Układ jest {system_type}.")
        return None


def get_rank(matrix):
    return matrix_rank(np.array(matrix))


def check_system(matrix):
    coeff_matrix = [row[:-1] for row in matrix]
    coeff_rank = get_rank(coeff_matrix)
    aug_rank = get_rank(matrix)
    num_unknowns = len(coeff_matrix[0])

    if coeff_rank == aug_rank == num_unknowns:
        return 'oznaczony'
    elif coeff_rank == aug_rank < num_unknowns:
        return 'nieoznaczony'
    else:
        return 'sprzeczny'
