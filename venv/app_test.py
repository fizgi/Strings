""" Test implementation class of the study
    which focuses on string methods, slices,
    working with files, and automated testing

    author: Fatih IZGI
    date: 21-Feb-2020
    version: python 3.8.1
"""

import unittest
from typing import List
from app import reverse, substring, find_second, get_lines


class ReverseTest(unittest.TestCase):
    """ Test class of the methods """
    def test_reverse(self):
        """ testing reverse """
        self.assertTrue(reverse('abc') == 'cba')
        self.assertTrue(reverse('Ab2tA77Khc') == 'chK77At2bA')

    def test_substring(self):
        """ testing substring """
        self.assertEqual(substring("he", "hello"), 0)
        self.assertEqual(substring("ell", "hello"), 1)
        self.assertEqual(substring("xxx", "hello"), -1)
        self.assertEqual(substring("asd", "sdfasdf"), 3)

    def test_find_second(self):
        """ testing find_second """
        self.assertTrue(find_second("iss", "Mississippi") == 4)
        self.assertTrue(find_second('abba', 'abbabba') == 3)
        self.assertTrue(find_second('abb', 'abbacc') == -1)
        self.assertTrue(find_second('23', '01230123') == 6)

    def test_get_lines(self):
        """ testing get_lines """
        file_name = "test_file.txt"

        result: List[str] = list(get_lines(file_name))
        expect: List[str] = ['<line0>', '<line1>', '<line2>', '<line3.1 line3.2 line3.3>',
                             '<line4.1 line4.2>', '<line5>', '<line6>']

        self.assertEqual(result, expect)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
