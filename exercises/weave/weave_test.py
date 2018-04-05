import unittest
from weave import weave
from queue import Queue

class TestWeaveMethods(unittest.TestCase):

    def test_equal_weave(self):
        q1 = Queue()
        q1.add(3)
        q1.add(4)
        q1.add(6)
        q2 = Queue()
        q2.add("Hi")
        q2.add("Ho")
        q2.add("He")
        self.assertEqual(weave(q1, q2).array, ["He", 6, "Ho", 4, "Hi", 3])

    def test_uneven_weave(self):
        q1 = Queue()
        q1.add(2)
        q1.add(3)
        q1.add(4)
        q1.add(6)
        q1.add(7)
        q2 = Queue()
        q2.add("Hi")
        q2.add("Ho")
        q2.add("He")
        self.assertEqual(weave(q1, q2).array, [7, 6, "He", 4, "Ho", 3, "Hi", 2])

if __name__ == '__main__':
    unittest.main()