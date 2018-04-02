import unittest
from reversestring import reverse, reverse_join, reverse_manual, reverse_array

class TestReverseStringMethods(unittest.TestCase):

    def test_isreversed(self):
        reverse_funcs = [reverse, reverse_array, reverse_manual, reverse_array]
        for func in reverse_funcs:
            self.assertEqual(func('apple'), 'elppa')
            self.assertEqual(func('hello'), 'olleh')
            self.assertEqual(func('Greetings!'), '!sgniteerG')

if __name__ == '__main__':
    unittest.main()