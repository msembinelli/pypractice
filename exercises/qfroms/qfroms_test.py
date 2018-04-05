import unittest
from qfroms import Qfroms

class TestQfromsMethods(unittest.TestCase):

    def test_add(self):
        qfs = Qfroms()
        qfs.add(1)
        qfs.add(2)
        qfs.add(3)
        self.assertEqual(qfs.in_stack.array, [3, 2, 1])

    def test_remove(self):
        qfs = Qfroms()
        qfs.add(1)
        qfs.add(2)
        qfs.add(3)
        self.assertEqual(qfs.remove(), 1)
        self.assertEqual(qfs.in_stack.array, [3, 2])

    def test_peek(self):
        qfs = Qfroms()
        qfs.add(1)
        qfs.add(2)
        qfs.add(3)
        self.assertEqual(qfs.peek(), 1)
        self.assertEqual(qfs.in_stack.array, [3, 2, 1])

if __name__ == '__main__':
    unittest.main()