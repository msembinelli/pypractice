import unittest
from fib import fib, fib_recursive, fib_memoization

class TestFibMethods(unittest.TestCase):

    def test_fib(self):
        funcs = [fib, fib_recursive, fib_memoization]
        for func in funcs:
            self.assertEqual(func(4), 3)

if __name__ == '__main__':
    unittest.main()