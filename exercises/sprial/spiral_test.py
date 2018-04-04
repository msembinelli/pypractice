import unittest
from sprial import spiral

class TestSpiralMethods(unittest.TestCase):

    def test_spiral(self):
        funcs = [spiral]
        for func in funcs:
            self.assertEqual(func(3), [[1,2,3], [8,9,4], [7,6,5]])

if __name__ == '__main__':
    unittest.main()