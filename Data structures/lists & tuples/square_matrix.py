#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = matrix.copy()
    for i in range(len(matrix)):
        for x in range(len(matrix[i])):
            new[i][x] = matrix[i][x]**2
    print(new)
def square_matrix_simple(matrix=[]):
    new = [list(map(lambda x: x**2, matrix[i])) for i in range(len(matrix))]
    print (new)
square_matrix_simple([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
