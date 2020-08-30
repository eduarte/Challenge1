from unittest import TestCase

from challenge1 import find_largest_word, reverse_string, read_from_file


class TestFindLargestWord(TestCase):
    def test_find_largest_word(self):
        data = ["a", "ab", "abc"]
        result = find_largest_word(data)
        self.assertEqual(result, "abc")

    def test_empty_array(self):
        data = []
        result = find_largest_word(data)
        self.assertEqual(result, "Not a valid list of strings")

    def test_int_array(self):
        data = [1, 2, 3, 4]
        self.assertRaises((TypeError, ValueError), find_largest_word(data), "Not a valid list of strings")


class TestReverseWord(TestCase):
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

    def test_int_provided(self):
        word = 1
        self.assertRaises((TypeError, ValueError), reverse_string(word), "Ops! Something went wrong, please try again with a valid word!")

    def test_no_word_provided(self):
        word = ""
        self.assertRaises((TypeError, ValueError), reverse_string(word), "Ops! Something went wrong, please try again with a valid word!")

