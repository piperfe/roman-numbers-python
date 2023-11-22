import unittest

from src.roman_numbers_generator import sum_numbers


class TestSumNumbers(unittest.TestCase):

    def test_sum_numbers(self):
        self.assertEqual(sum_numbers(1, 2), 3)