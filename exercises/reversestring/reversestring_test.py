import unittest
from reversestring import reverse, reverse_join, reverse_manual, reverse_array

class TestReverseStringMethods(unittest.TestCase):

    def test_isreversed(self):
        self.assertEqual(reverse('apple'), 'elppa')
        self.assertEqual(reverse('hello'), 'olleh')
        self.assertEqual(reverse('Greetings!'), '!sgniteerG')

    def test_isreversed_join(self):
        self.assertEqual(reverse_join('apple'), 'elppa')
        self.assertEqual(reverse_join('hello'), 'olleh')
        self.assertEqual(reverse_join('Greetings!'), '!sgniteerG')

    def test_isreversed_manual(self):
        self.assertEqual(reverse_manual('apple'), 'elppa')
        self.assertEqual(reverse_manual('hello'), 'olleh')
        self.assertEqual(reverse_manual('Greetings!'), '!sgniteerG')

    def test_isreversed_array(self):
        self.assertEqual(reverse_array('apple'), 'elppa')
        self.assertEqual(reverse_array('hello'), 'olleh')
        self.assertEqual(reverse_array('Greetings!'), '!sgniteerG')

if __name__ == '__main__':
    unittest.main()