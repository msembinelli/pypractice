import unittest
from stack import Stack

class TestStackMethods(unittest.TestCase):

    def test_push(self):
        s = Stack()
        s.push(3)
        s.push(4)
        s.push(6)
        self.assertEqual(s.array, [6,4,3])

    def test_pop(self):
        s = Stack()
        s.push(3)
        s.push(4)
        s.push(6)
        self.assertEqual(s.pop(), 6)
        self.assertEqual(s.array, [4,3])

    def test_peek(self):
        s = Stack()
        s.push(3)
        s.push(4)
        s.push(6)
        self.assertEqual(s.peek(), 6)

if __name__ == '__main__':
    unittest.main()