import unittest
from queue import Queue

class TestQueueMethods(unittest.TestCase):

    def test_add(self):
        q = Queue()
        q.add(3)
        q.add(4)
        q.add(6)
        self.assertEqual(q.array, [6,4,3])

    def test_remove(self):
        q = Queue()
        q.add(3)
        q.add(4)
        q.add(6)
        self.assertEqual(q.remove(), 3)

if __name__ == '__main__':
    unittest.main()