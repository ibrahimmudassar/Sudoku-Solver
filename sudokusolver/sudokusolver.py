"""
This module contains the core functions to solve Sudoku puzzle.
The module has a soft dependency on sudokusolver.plotutilities,
which is used to graphically render the Sudoku solution. This
module will still run without plotutilities. This module depends
on numpy library.
"""
__author__ = 'krishnakumarramamoorthy'

import time
import sys
import os
from math import ceil

try:
    import plotutilities as plotter
    is_matplotlib_available = True
except ImportError:
    is_matplotlib_available = False
    print 'Plotting module could not be imported. Only textual output will be provided'
import xumpy as xp


def main():
    """
    Main method for the sudoku solver. Takes path to csv file
    containing the problem as input. Prints the solution on
    console window. Write the solution to
    <input_file_name>-out.csv file. If Matplotlib is available,
    then displays the solution graphically and saves a screenshot
    to <input_file_name>-out.png

    Optional argument: </path/to/csv/problem/file>
        Default: '/data/input.csv'
        The input file is expected to be contain 9 lines,
        with each line containing 9 values separated by comma.
        Unfilled cells will be identified by 0 (zero).
    """
    path = PROJECT_ROOT + '/data/input.csv'
    try:
        if len(sys.argv) > 1:
            path = sys.argv[1]
    except:
        print 'Using default input file in ' + path
    [input_matrix, zero_indices] = load_input(path)
    # init
    current_zero_index = -1
    stats = {'index': [], 'values': []}
    ts = time.time()
    # pass a deep copy of input_matrix to solver
    [solved_matrix, stats] = solve(xp.copy(input_matrix), zero_indices, current_zero_index, stats)
    time_to_solution = time.time() - ts
    out_path = path.replace('.csv', '_out.csv')
    write_solution(solved_matrix, out_path)
    print_solution(solved_matrix, time_to_solution, len(stats['index']))
    if is_matplotlib_available:
        fig_out_path = path.replace('.csv', '_out')
        plotter.visualize_solution(input_matrix, solved_matrix, stats, zero_indices, ts, fig_out_path, time_to_solution)
    else:
        print 'Matplotlib import not successful. Cannot graphically display solution.'
    return solved_matrix, stats


def solve(matrix, zero_indices, current_zero_index, stats):
    """
    Implementation of recursive backtracking algorithm to solve the sudoku matrix
    """
    current_zero_index += 1
    if current_zero_index >= len(zero_indices[0]):
        return [matrix, stats]
    row = zero_indices[0][current_zero_index]
    col = zero_indices[1][current_zero_index]
    prev_zero_index_value = matrix[zero_indices[0][current_zero_index - 1]][zero_indices[1][current_zero_index - 1]]
    number = 0
    for number in range(1, 10):
        # store tuples for creating links
        stats['index'].append((current_zero_index - 1, current_zero_index))
        stats['values'].append((prev_zero_index_value, number))
        # check if the solution satisfies all - column, row and region - rules
        is_acceptable = evaluate_solution(matrix, row, col, number)
        if is_acceptable:
            matrix[row][col] = number
            [solution, stats] = solve(matrix, zero_indices, current_zero_index, stats)
            if solution is not None:
                return [solution, stats]
    if number is 9:
        return [None, stats]


def evaluate_solution(matrix, i, j, n):
    """
    Checks if the value for cell[i][j] is a valid solution
    """
    matrix[i][j] = 0
    row_length = 1
    region_repeat = 1
    valid = False
    col_length = len((xp.where(matrix[i], n))[0])
    if col_length is 0:
        row_length = len((xp.where(xp.get_sub_matrix(matrix, 0, 9, j, j + 1), n))[0])
    if row_length is 0:
        i_region = int(ceil((i + 1) / 3.0) - 1)
        j_region = int(ceil((j + 1) / 3.0) - 1)
        region_matrix = xp.get_sub_matrix(matrix, i_region * 3, i_region * 3 + 3, j_region * 3, j_region * 3 + 3)
        region_repeat = (len((xp.where(region_matrix, n))[0]) + len((xp.where(region_matrix, n))[1]))
    if region_repeat is 0:
        valid = True
    return valid


def print_solution(solved_matrix, time_to_solution, iterations):
    print '============= Stats ============='
    print 'Time to solution: {:.4f} secs'.format(time_to_solution)
    print 'Total iterations: {}'.format(iterations)
    print '=========== Solution ============'
    for row in solved_matrix:
        print row
    print '================================='
    validate_solution(solved_matrix)


def load_input(path):
    """
    Loads problem file and checks if it is a valid sudoku matrix
    """
    input_matrix = xp.loadtxt(path, dtype=int, delimiter=',')
    validate_input(input_matrix)
    # find all the unfilled cells, currently set to 0
    zero_indices = xp.where(input_matrix, 0)
    return input_matrix, zero_indices


def validate_input(input_matrix):
    assert len(input_matrix) == 9, 'Input matrix does not have 9 rows'
    assert len(input_matrix[0]) == 9, 'Input matrix does not have 9 cols'
    assert len((xp.where(input_matrix, 0))[0]) > 0, 'Input matrix does not have any unfilled cells'


def validate_solution(solved_matrix):
    for i in range(9):
        assert len(set(solved_matrix[i])) == 9, 'Solution invalid: Row {} is not unique'.format(i + 1)
        assert len(set(sum(xp.get_sub_matrix(solved_matrix, 0, 9, i, i + 1),
                    []))) == 9, 'Solution invalid: Col {} is not unique'.format(i + 1)
        j = divmod(i + 1, 3)[1]
        i_region = int(ceil((i + 1) / 3.0) - 1)
        j_region = int(ceil((j + 1) / 3.0) - 1)
        assert (len(set(sum(xp.get_sub_matrix(solved_matrix, i_region * 3, i_region * 3 + 3,
                                              j_region * 3, j_region * 3 + 3), []))) == 9), \
            ('Solution invalid: Region {},{} is not unique'.format(i + 1, j + 1))


def write_solution(solved_matrix, out_path):
    xp.savetxt(out_path, solved_matrix, fmt='%d', delimiter=',')


if __name__ == "__main__":
    PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__)).replace('\\', '/').rsplit('/', 1)[0]
    main()