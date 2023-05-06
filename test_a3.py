"""CSCA08: Fall 2022 -- Assignment 3: Hypertension and Low Income

Starter code for tests to test function get_bigger_neighbourhood in
a3.py.

This code is provided solely for the personal and private use of
students taking the CSC108/CSCA08 course at the University of
Toronto. Copying for purposes other than this use is expressly
prohibited. All forms of distribution of this code, whether as given
or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2022 Jacqueline Smith, David Liu, and Anya Tafliovich

"""

import copy
import unittest
from a3 import get_bigger_neighbourhood as gbn
from a3 import SAMPLE_DATA

SAMPLE_DATA2 = {
    'A': {
        'id': 1,
        'hypertension': [703, 13291, 3741, 9663, 3959, 5176],
        'total': 222222, 'low_income': 5950},
    'B': {
        'id': 2,
        'hypertension': [789, 12906, 3578, 8815, 2927, 3902],
        'total': 222222, 'low_income': 9690},
    'C': {
        'id': 3,
        'hypertension': [220, 3631, 1047, 2829, 1349, 1767],
        'total': 0, 'low_income': 2005},
    'D': {
        'id': 4,
        'hypertension': [201, 3669, 1134, 3229, 1393, 1854],
        'total': 0, 'low_income': 2140},
    'E': {
        'id': 5,
        'hypertension': [176, 3353, 1040, 2842, 948, 1322],
        'total': 9466, 'low_income': 2315}
}

SAMPLE_DATA3 = {
    'A': {
        'id': 1,
        'hypertension': [703, 13291, 3741, 9663, 3959, 5176],
        'total': 222222, 'low_income': 5950},
    'B': {
        'id': 2,
        'hypertension': [789, 12906, 3578, 8815, 2927, 3902],
        'total': 222222, 'low_income': 9690},
    'C': {
        'id': 3,
        'hypertension': [220, 3631, 1047, 2829, 1349, 1767],
        'total': 0, 'low_income': 2005},
    'D': {
        'id': 4,
        'hypertension': [201, 3669, 1134, 3229, 1393, 1854],
        'total': 0, 'low_income': 2140},
    'E': {
        'id': 0,
        'hypertension': [176, 3353, 1040, 2842, 948, 1322],
        'total': 9466, 'low_income': 2315}
}


class TestGetBiggerNeighbourhood(unittest.TestCase):
    """Test the function get_bigger_neighbourhood."""

    def test_first_bigger(self):
        """Test that get_bigger_neighbourhood correctly returns the first
        neighbourhood when its population is strictly greater than the
        population of the second neighbourhood.

        """

        sample_data_copy = copy.deepcopy(SAMPLE_DATA)
        expected = 'Rexdale-Kipling'
        actual = gbn(SAMPLE_DATA, 'Elms-Old Rexdale', 'Rexdale-Kipling')
        msg = message(sample_data_copy, expected, actual)
        self.assertEqual(actual, expected, msg)


    def test_second_bigger(self):
        """Test that get_bigger_neighbourhood correctly returns the second
        neighbourhood when its population is strictly greater than the
        population of the first neighbourhood.

        """

        sample_data_copy = copy.deepcopy(SAMPLE_DATA)
        expected = 'Rexdale-Kipling'
        actual = gbn(SAMPLE_DATA, 'Rexdale-Kipling', 'Elms-Old Rexdale')
        msg = message(sample_data_copy, expected, actual)
        self.assertEqual(actual, expected, msg)


    def test_same_size(self):
        """Test that get_bigger_neighbourhood correctly returns the first
        parameter neighbourhood when both neighbourhoods have the same
        population.

        """

        sample_data_copy = copy.deepcopy(SAMPLE_DATA2)
        expected = 'B'
        actual = gbn(SAMPLE_DATA, 'B', 'A')
        msg = message(sample_data_copy, expected, actual)
        self.assertEqual(actual, expected, msg)


    def test_first_unknown_second_known(self):
        """Test that get_bigger_neighbourhood correctly returns the bigger
        neighbourhood when the first parameter is not a known neighbourhood
        but the second parameter is.

        """

        sample_data_copy = copy.deepcopy(SAMPLE_DATA)
        expected = 'Rexdale-Kipling'
        actual = gbn(SAMPLE_DATA, 'A', 'Rexdale-Kipling')
        msg = message(sample_data_copy, expected, actual)
        self.assertEqual(actual, expected, msg)


    def test_first_known_second_unknown(self):
        """Test that get_bigger_neighbourhood correctly returns the bigger
        neighbourhood when the first parameter is a known neighbourhood
        but the second parameter is not.

        """

        sample_data_copy = copy.deepcopy(SAMPLE_DATA)
        expected = 'Rexdale-Kipling'
        actual = gbn(SAMPLE_DATA, 'Rexdale-Kipling', 'A')
        msg = message(sample_data_copy, expected, actual)
        self.assertEqual(actual, expected, msg)


    def test_both_unknown(self):
        """Test that get_bigger_neighbourhood correctly returns the first
        parameter when both neighbourhoods are unknown.

        """

        sample_data_copy = copy.deepcopy(SAMPLE_DATA)
        expected = 'A'
        actual = gbn(SAMPLE_DATA, 'A', 'B')
        msg = message(sample_data_copy, expected, actual)
        self.assertEqual(actual, expected, msg)


    def test_both_zero(self):
        """Test that get_bigger_neighbourhood correctly returns the first
        parameter when both neighbourhoods have a population of 0.

        """

        sample_data_copy = copy.deepcopy(SAMPLE_DATA)
        expected = 'C'
        actual = gbn(SAMPLE_DATA, 'C', 'D')
        msg = message(sample_data_copy, expected, actual)
        self.assertEqual(actual, expected, msg)


    def test_one_unknown_other_zero(self):
        """Test that get_bigger_neighbourhood correctly returns the first
        parameter when one neighbourhood is unknown and the other neighbourhood
        has a population of 0.

        """

        sample_data_copy = copy.deepcopy(SAMPLE_DATA)
        expected = 'F'
        actual = gbn(SAMPLE_DATA, 'F', 'E')
        msg = message(sample_data_copy, expected, actual)
        self.assertEqual(actual, expected, msg)


def message(test_case: dict, expected: list, actual: object) -> str:
    """Return an error message saying the function call
    get_most_published_authors(test_case) resulted in the value
    actual, when the correct value is expected.

    """

    return ("When we called get_most_published_authors(" + str(test_case) +
            ") we expected " + str(expected) +
            ", but got " + str(actual))


if __name__ == '__main__':
    unittest.main(exit=False)
