import unittest
from anagram import is_anagram, is_anagram_better, is_anagram_sort

class TestChunkMethods(unittest.TestCase):

    def test_chunk(self):
        funcs = [is_anagram, is_anagram_better, is_anagram_sort]
        for func in funcs:
            self.assertTrue(func('rail safety', 'fairy tales'))
            self.assertTrue(func('RAIL! SAFETY!', 'fairy tales'))
            self.assertFalse(func('Hi there', 'Bye there'))

if __name__ == '__main__':
    unittest.main()