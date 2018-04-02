import unittest
from maxchar import max_char

class TestMaxCharMethods(unittest.TestCase):

    def test_maxchar(self):
        funcs = [max_char]
        for func in funcs:
            self.assertEqual(func('abccccccd'), 'c')
            self.assertEqual(func('apple 1231111'), '1')

if __name__ == '__main__':
    unittest.main()