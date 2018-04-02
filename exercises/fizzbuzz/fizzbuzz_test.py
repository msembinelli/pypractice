import unittest
from fizzbuzz import fizz_buzz

import sys
from contextlib import contextmanager
from StringIO import StringIO

@contextmanager
def captured_output():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err

class TestFizzBuzzMethods(unittest.TestCase):

    def test_fizzbuzz(self):
        with captured_output() as (out, err):
            fizz_buzz(5)
        output = out.getvalue().strip()
        self.assertEqual(output, '1\n2\nfizz\n4\nbuzz')

        with captured_output() as (out, err):
            fizz_buzz(15)
        output = out.getvalue().strip()
        self.assertEqual(output, '1\n2\nfizz\n4\nbuzz\nfizz\n7\n8\nfizz\nbuzz\n11\nfizz\n13\n14\nfizzbuzz')

if __name__ == '__main__':
    unittest.main()