import unittest
from palindrome import is_palindrome, is_palindrome_element

class TestPalindromeMethods(unittest.TestCase):

    def test_ispalindrome(self):
        funcs = [is_palindrome, is_palindrome_element]
        for func in funcs:
            self.assertTrue(func('abba'))
            self.assertTrue(func('10001'))
            self.assertFalse(func('hello'))

if __name__ == '__main__':
    unittest.main()