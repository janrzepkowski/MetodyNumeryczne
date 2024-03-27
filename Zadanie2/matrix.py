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

# creates A|I|b
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
                # znajduje wartość kolejną po nowoutworzonej 1
                coeff_to_zero = matrix[k][i]
                # dla każego z
                for j in range(2*column_length + 1):
                    matrix[k][j] -= coeff_to_zero * matrix[i][j]
    return matrix


# ------------------------------------------------------

test = [
    [2, 4, 1, 7],
    [1, 1, 1, 10],
    [4, 1, 7, 12]
]

n_x_2n = attach_unit_matrix(test)

for i in n_x_2n:
    print(i)

print()
solved = gauss_jordan(n_x_2n)

for i in solved:
    print(i)
