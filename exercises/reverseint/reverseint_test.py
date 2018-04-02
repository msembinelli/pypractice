import unittest
from reverseint import reverse_int, reverse_int_mod

class TestReverseIntMethods(unittest.TestCase):

    def test_reverseint(self):
        funcs = [reverse_int, reverse_int_mod]
        for func in funcs:
            self.assertEqual(func(15), 51)
            self.assertEqual(func(981), 189)
            self.assertEqual(func(5), 5)
            self.assertEqual(func(-15), -51)
            self.assertEqual(func(-90), -9)

if __name__ == '__main__':
    unittest.main()