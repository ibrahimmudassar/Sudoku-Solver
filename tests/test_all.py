#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_all
----------------------------------

Tests for `sudokusolver`, `plotutilities` and  `xumpy`.
"""

import unittest
import os

from sudokusolver import sudokusolver
from sudokusolver import xumpy as np


class TestAll(unittest.TestCase):

    def setUp(self):
        self.project_root = os.path.dirname(os.path.realpath(__file__)).replace('\\', '/').rsplit('/', 1)[0]
        self.test_problem = np.loadtxt(self.project_root+'/data/test_problem.csv', dtype=int, delimiter=',')
        self.expected_solution = np.loadtxt(self.project_root+'/data/test_solution.csv', dtype=int, delimiter=',')
        self.current_zero_index = -1
        self.zero_indices = [
                                [0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 8, 8, 8, 8],
                                [0, 5, 0, 5, 7, 5, 6, 8, 6, 8, 0, 1, 2, 4, 8, 0, 3, 8, 1, 6, 7, 3, 1, 2, 4, 5]
                            ]
        self.stats = {'index': [], 'values': []}
        pass

    def tearDown(self):
        pass

    def test_load(self):
        [input_matrix, zero_indices] = sudokusolver.load_input(self.project_root+'/data/test_problem.csv')
        self.assertEqual(len(zero_indices[0]), 26, 'Number of unfilled cells is incorrect.')

    def test_solver(self):
        [solved_matrix, stats] = sudokusolver.solve(self.test_problem, self.zero_indices,
                                                    self.current_zero_index, self.stats)
        self.assertEqual(np.comparematrix(solved_matrix, self.expected_solution), True, 'Solution incorrect.')

    def test_evaluate_solution(self):
        result = sudokusolver.evaluate_solution(self.test_problem, 0, 0, 2)
        self.assertEqual(result, False, 'Evaluate solution not working as expected.')
        result = sudokusolver.evaluate_solution(self.expected_solution, 0, 0, 7)
        self.assertEqual(result, False, 'Evaluate solution not working as expected.')
        result = sudokusolver.evaluate_solution(self.test_problem, 0, 0, 1)
        self.assertEqual(result, True, 'Evaluate solution not working as expected.')

    def test_validate_input(self):
        temp = np.zeros(2, 2)
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
        temp = np.copy(self.expected_solution)
        temp[0][0] = 2
        try:
            sudokusolver.validate_solution(temp)
            error = False
        except:
            error = True
        self.assertEqual(error, True)

    def test_copy(self):
        matrix = [[0, 0], [1, 1]]
        copy1 = matrix
        copy2 = np.copy(matrix)
        matrix[0][1] = 1
        self.assertFalse(copy1[0][1] == copy2[0][1], '(deep) Copy not working correctly')

    def test_where(self):
        matrix = [[0, 1], [2, 3]]
        matches = np.where(matrix, 2)
        self.assertTrue(matches[0][0] == 1 and matches[1][0] == 0, 'Where is not working correctly')

    def test_get_sub_matrix(self):
        matrix = [[0, 1, 2], [2, 3, 4]]
        sub_matrix = np.get_sub_matrix(matrix, 0, 1, 1, 3)
        self.assertTrue(sub_matrix[0][0] == 1 and sub_matrix[0][1] == 2, 'Get sub matrix not working correctly')

    def test_compare_matrix(self):
        matrixa = [[0, 1, 2], [2, 3, 4]]
        matrixb = [[0, 1, 2], [2, 3, 4]]
        self.assertTrue(np.comparematrix(matrixa, matrixb), 'Compare matrix not working correctly')
        matrixa[0][2] = 1
        self.assertFalse(np.comparematrix(matrixa, matrixb), 'Compare matrix not working correctly')
