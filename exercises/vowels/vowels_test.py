import unittest
from vowels import vowels, vowels_regex

class TestVowelsMethods(unittest.TestCase):

    def test_vowels(self):
        funcs = [vowels, vowels_regex]
        for func in funcs:
            self.assertEqual(func('Hi There!'), 3)
            self.assertEqual(func('Why do you ask?'), 4)
            self.assertEqual(func('Why?'), 0)

if __name__ == '__main__':
    unittest.main()