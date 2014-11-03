"""
Xumpy module contains functions, which are available in numpy,
required by Sudoku solver. This module is created to eliminate
Sudoku solver dependency on numpy.
"""
__author__ = 'krishnakumarramamoorthy'

import random


def copy(matrix):
    """
    Make a deep copy
    """
    row = len(matrix)
    col = len(matrix[0])

    new_matrix = []

    for i in range(row):
        temp = []
        for j in range(col):
            temp.append(matrix[i][j])
        new_matrix.append(temp)

    return new_matrix


def where(matrix, val):
    """
    Identifies indices in the matrix which has val
    """
    row = len(matrix)
    xmatches = []
    ymatches = []

    try:
        col = len(matrix[0])
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == val:
                   xmatches.append(i)
                   ymatches.append(j)
    except:
        for i in range(row):
            if matrix[i] == val:
               xmatches.append(i)
               ymatches.append(0)

    return [xmatches,ymatches]


def reshape(matrix, nrow, ncol):
    row = len(matrix)
    col = len(matrix[0])

    flat_array = []

    new_matrix = []

    counter = 0
    for i in range(row):
        for j in range(col):
            flat_array[counter] = matrix[i][j]
            counter += 1

    for i in range(nrow):
        temp = []
        for j in range(ncol):
                temp.append(flat_array[counter])
        new_matrix.append(temp)

    return new_matrix


def loadtxt(path, **kwargs):
    matrix = []
    with open(path, 'r') as f:
        for line in f:
            fields = line.split(",")
            temp = []
            for item in fields:
                temp.append(int(item))
            matrix.append(temp)

    return matrix


def savetxt(path, matrix, **kwargs):
    with open(path, 'w') as f:
        text = ''

        for array in matrix:
            for val in array:
                text += str(val)+','
            text = text[0:-1]
            text += '\n'

        f.write(text)


def get_sub_matrix(matrix, start_row, end_row, start_col, end_col):
    """
    Gets slice of list of lists
    """
    return [row[start_col:end_col] for row in matrix[start_row:end_row]]


def arange(start, stop, increment):
    array = []
    counter = 0
    while True:
        new_val = start + increment*counter
        counter += 1
        if (new_val >= stop):
            break
        array.append(new_val)
    return array


def randn(x, y, max_val):
    matrix = []

    for i in range(x):
        temp = []
        for j in range(y):
            temp.append(random.randint(1, max_val))
        matrix.append(temp)

    return matrix


