import unittest
from capitalize import capitalize_string, capitalize_string_char

class TestCapitalizeMethods(unittest.TestCase):

    def test_capitalize(self):
        funcs = [capitalize_string, capitalize_string_char]
        for func in funcs:
            self.assertEqual(func('a short sentence'), 'A Short Sentence')
            self.assertEqual(func('a lazy fox'), 'A Lazy Fox')
            self.assertEqual(func('look, it is working!'), 'Look, It Is Working!')
            self.assertEqual(func('look, it is working !'), 'Look, It Is Working !')

if __name__ == '__main__':
    unittest.main()