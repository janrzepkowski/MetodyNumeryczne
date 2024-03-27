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

# ---------------------------------------------------------------

# TODO: napisać funkcję weryfikującą czy układ jest oznaczony
# TODO: jeśli nie to jaki? -> zwróć błąd/log

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
def print_m(matrix):
    for i in matrix:
        print(i)
    print()


# właściwa metoda rozwiania A|I|b -> I|A^-1|X, gdzie X - rozwiązania
def gauss_jordan(matrix):
    column_length = len(matrix)
    row_length = len(matrix[0])

    for i in range(column_length):
        # jeśli na przekątnej nie ma 1, to dzieli wiersz przez tę liczbę
        if matrix[i][i] != 1:
            i_value = matrix[i][i]

            for j in range(row_length):
                matrix[i][j] /= i_value

        # jeśli kolumna nie jest postaci jednostkowej to:
        for k in range(column_length):
            if k != i:
                # znajduje wartość w kolejnym wierszu
                coeff_to_zero = matrix[k][i]

                # każde pole w danym wierszu jest pomniejszone o (wartość coeff) * (wartość z kolumny wyżej)
                # działanie równoznaczne z odjęciem od siebie współczynników kolumn,
                # po uprzednim pomnożeniu np. w1 - 3*w2

                for j in range(2 * column_length + 1):
                    matrix[k][j] -= coeff_to_zero * matrix[i][j]

    return matrix


# wyciąga rozwiązania z I|A^-1|X
def get_solution(matrix):
    solution = []
    row_length = len(matrix[0])

    for i in matrix:
        solution.append(i[row_length - 1])

    return solution


# funkcja do wywołania
def find_solution(matrix):
    matrix_unit_solution = attach_unit_matrix(matrix)
    print_m(matrix_unit_solution)

    solved = gauss_jordan(matrix_unit_solution)
    print_m(solved)

    solution = get_solution(solved)

    return solution
