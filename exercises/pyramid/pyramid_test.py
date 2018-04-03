import unittest
from pyramid import pyramid

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

class TestPyramidMethods(unittest.TestCase):

    def test_pyramid(self):
        funcs = [pyramid]
        for func in funcs:
            with captured_output() as (out, err):
                func(3)
            output = out.getvalue().rstrip()
            self.assertEqual(output, '  #  \n ### \n#####')

if __name__ == '__main__':
    unittest.main()