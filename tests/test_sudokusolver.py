#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_sudokusolver
----------------------------------

Tests for `sudokusolver` module.
"""

import unittest
import os
from numpy import loadtxt, zeros, copy

from sudokusolver import sudokusolver


class TestSudokusolver(unittest.TestCase):

    def setUp(self):
        self.PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__)).rsplit('/',1)[0]
        self.test_problem = loadtxt(self.PROJECT_ROOT+'/data/test_problem.csv', dtype=int, delimiter=',')
        self.expected_solution = loadtxt(self.PROJECT_ROOT+'/data/test_solution.csv', dtype=int, delimiter=',')
        self.current_zero_index = -1
        self.zero_indices = [[0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 8, 8, 8, 8],
                             [0, 5, 0, 5, 7, 5, 6, 8, 6, 8, 0, 1, 2, 4, 8, 0, 3, 8, 1, 6, 7, 3, 1, 2, 4, 5]
                            ]
        self.stats = {'index': [], 'values': []}
        pass


    def tearDown(self):
        pass


    def test_load(self):
        [input_matrix, zero_indices] = sudokusolver.load_input(self.PROJECT_ROOT+'/data/test_problem.csv')
        self.assertEqual(len(self.zero_indices[0]), 26, 'Number of unfilled cells is incorrect.')


    def test_solver(self):
        [solved_matrix, stats] = sudokusolver.solve(self.test_problem, self.zero_indices,
                                                    self.current_zero_index, self.stats)
        self.assertEqual(solved_matrix.all(), self.expected_solution.all(), 'Solution incorrect.')


    def test_evaluate_solution(self):
        result = sudokusolver.evaluate_solution(self.test_problem, 0, 0, 2)
        self.assertEqual(result, False, 'Evaluate solution not working as expected.')
        result = sudokusolver.evaluate_solution(self.expected_solution, 0, 0, 7)
        self.assertEqual(result, False, 'Evaluate solution not working as expected.')
        result = sudokusolver.evaluate_solution(self.test_problem, 0, 0, 1)
        self.assertEqual(result, True, 'Evaluate solution not working as expected.')


    def test_validate_input(self):
        temp = zeros((2,2))
        try:
            sudokusolver.validate_input(temp)
            error = False
        except:
            error = True
        self.assertEqual(error, True)

        try:
            sudokusolver.validate_input(self.test_problem)
            error = False
        except:
            error = True
        self.assertEqual(error, False)


    def test_validate_solution(self):
        try:
            sudokusolver.validate_solution(self.expected_solution)
            error = False
        except:
            error = True
        self.assertEqual(error, False)

        temp = copy(self.expected_solution)
        temp[0, 0] = 2
        try:
            sudokusolver.validate_solution(temp)
            error = False
        except:
            error = True
        self.assertEqual(error, True)


if __name__ == '__main__':
    unittest.main()
