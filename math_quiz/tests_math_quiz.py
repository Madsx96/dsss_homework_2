"""----------------------------------------------------------------------------------------------
 Name:          test_math_quiz.py
 Purpose:       This script contains unit tests for the Math Quiz Game,
 Modified by:   Mohammad Ali Karimi (mohammadali.karimi@fau.de)
 Interpreter:   PYTHON version 3.11.5
 Created:       2023/11/13
 Licence:       Apache 2.0
----------------------------------------------------------------------------------------------
"""


import unittest
from math_quiz import number_generator, operator_generator, solver


class TestMathGame(unittest.TestCase):
    """
    class of unit tests
    """
    def test_number_generator(self):
        """
        Test if random numbers generated are within the specified range
        """
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = number_generator(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)
            
            
    def test_operator_generator(self):
        """
        test if random operator generated is one of +/-/*
        """
        for _ in range(1000):
            rand_op = operator_generator()
            self.assertIn(rand_op, ['+', '-', '*'])


    def test_solver(self):
        """
        test if the calculation method is working properly
        """
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (10, 10, '*', '10 * 10', 100),
            (-1, 1, '+', '-1 + 1', 0),
            (-1, 1, '-', '-1 - 1', -2),
            (-1, -1, '*', '-1 * -1', 1),
            (-1, 1, '*', '-1 * 1', -1),
        ]

        for number_1, number_2, operator, expected_problem, expected_answer in test_cases:
            result_problem, result_answer = solver(number_1, number_2, operator)
            self.assertEqual(expected_problem, result_problem)
            self.assertEqual(expected_answer, result_answer)

if __name__ == "__main__":
    unittest.main()
