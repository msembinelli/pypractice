import unittest
from chunk import array_chunk, array_chunk_slice

class TestChunkMethods(unittest.TestCase):

    def test_chunk(self):
        funcs = [array_chunk, array_chunk_slice]
        for func in funcs:
            self.assertEqual(func([1, 2, 3, 4], 2), [[1, 2], [3, 4]])
            self.assertEqual(func([1, 2, 3, 4, 5], 2), [[1, 2], [3, 4], [5]])

if __name__ == '__main__':
    unittest.main()