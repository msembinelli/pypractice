import unittest
from linkedlist import Node, Linkedlist

class TestLinkedlistMethods(unittest.TestCase):

    def test_insert_first(self):
        n = Node(1)
        ll = Linkedlist()
        ll.insert_first(n)
        self.assertEqual(ll.head, n)
        self.assertEqual(ll.head.data, n.data)

    def test_get_first(self):
        n = Node(1)
        ll = Linkedlist()
        ll.insert_first(n)
        self.assertEqual(ll.get_first(), n)

    def test_remove_first(self):
        n = Node(1)
        ll = Linkedlist()
        ll.insert_first(n)
        self.assertEqual(ll.remove_first(), n)
        self.assertEqual(ll.get_first(), None)

    def test_insert_last(self):
        n = Node(1)
        ll = Linkedlist()
        ll.insert_last(n)
        self.assertEqual(ll.get_last(), n)

    def test_get_last(self):
        n = Node(1)
        ll = Linkedlist()
        self.assertEqual(ll.get_last(), None)
        ll.insert_last(n)
        self.assertEqual(ll.get_last(), n)

    def test_remove_last(self):
        n = Node(1)
        ll = Linkedlist()
        self.assertEqual(ll.remove_last(), None)
        ll.insert_last(n)
        self.assertEqual(ll.remove_last(), n)
        self.assertEqual(ll.size, 0)
        n = Node(2)
        ll.insert_last(n)
        n = Node(3)
        ll.insert_last(n)
        self.assertEqual(ll.remove_last(), n)

    def test_insert_at(self):
        n = Node(1)
        ll = Linkedlist()
        ll.insert_at(0, n)
        self.assertEqual(ll.get_at(0), n)
        n = Node(2)
        ll.insert_at(10, n)
        self.assertEqual(ll.get_at(1), n)

    def test_get_at(self):
        n = Node(1)
        ll = Linkedlist()
        ll.insert_at(0, n)
        self.assertEqual(ll.get_at(0), n)
        n = Node(2)
        ll.insert_at(10, n)
        self.assertEqual(ll.get_at(1), n)

    def test_remove_at(self):
        n1 = Node(1)
        ll = Linkedlist()
        self.assertEqual(ll.remove_at(0), None)
        ll.insert_at(0, n1)
        n2 = Node(2)
        ll.insert_at(10, n2)
        n3 = Node(3)
        ll.insert_at(1, n3)
        self.assertEqual(ll.remove_at(2), n3)
        self.assertEqual(ll.remove_at(0), n1)

    def test_clear(self):
        n = Node(1)
        ll = Linkedlist()
        ll.insert_first(n)
        ll.clear()
        self.assertEqual(ll.get_first(), None)

    def test_iter(self):
        ll = Linkedlist()
        n1 = Node(1)
        ll.insert_at(0, n1)
        n2 = Node(2)
        ll.insert_at(10, n2)
        n3 = Node(3)
        ll.insert_at(1, n3)
        for node in ll:
            print node.data


if __name__ == '__main__':
    unittest.main()