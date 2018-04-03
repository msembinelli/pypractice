import unittest
from steps import step, step_naive

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

class TestStepsMethods(unittest.TestCase):

    def test_steps(self):
        funcs = [step, step_naive]
        for func in funcs:
            with captured_output() as (out, err):
                func(5)
            output = out.getvalue().strip()
            self.assertEqual(output, '#    \n##   \n###  \n#### \n#####')

if __name__ == '__main__':
    unittest.main()