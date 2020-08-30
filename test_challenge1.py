import unittest.mock as mock
from unittest import TestCase
from unittest.mock import mock_open

from challenge1 import find_largest_word, reverse_string, read_from_file


class Test(TestCase):
    def test_find_largest_word(self):
        data = ["a", "ab", "abc"]
        result = find_largest_word(data)
        self.assertEqual(result, "abc")


class Test(TestCase):
    def test_reverse_string(self):
        word = "qwerty"
        reversed_word = "ytrewq"
        result = reverse_string(word)
        self.assertEqual(result, reversed_word)

    def test_word_not_reversed(self):
        word = "qwerty"
        reversed_word = "ytrewq"
        result = reverse_string(word)
        self.assertNotEqual(result, word)

