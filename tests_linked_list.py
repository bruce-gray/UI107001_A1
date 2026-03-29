import unittest
from linked_list import LinkedList

class TestLinkedList(unittest.TestCase):

    # tests regular inserts
    def test_insert(self):
        ll = LinkedList()
        ll.insert(0)
        ll.insert(18)
        ll.insert(-5)
        ll.insert(3.14)
        self.assertTrue(ll.search(0))
        self.assertTrue(ll.search(18))
        self.assertTrue(ll.search(-5))
        self.assertTrue(ll.search(3.14))

    # tests inserts with duplicate data
    def test_duplicate_insert(self):
        ll = LinkedList()
        ll.insert(5)
        ll.insert(5)
        self.assertTrue(ll.search(5))

    # search for a value that exists in the linked list
    def test_search_found(self):
        ll = LinkedList()
        ll.insert(18)
        self.assertTrue(ll.search(18))

    # search for a value that does not exist in the linked list
    def test_search_missing(self):
        ll = LinkedList()
        ll.insert(24)
        ll.insert(26)
        self.assertFalse(ll.search(25))

    # search for this value while the linked list is empty
    def test_search_empty(self):
        ll = LinkedList()
        self.assertFalse(ll.search(1))

    # delete a regular value
    def test_delete(self):
        ll = LinkedList()
        ll.insert(1)
        ll.insert(2)
        ll.insert(3)
        self.assertTrue(ll.search(2))
        ll.delete(2)
        self.assertFalse(ll.search(2))

    # delete the head node (first value), and then check that subsequent values can still be found through search
    def test_delete_head(self):
        ll = LinkedList()
        ll.insert(1)
        ll.insert(2)
        ll.insert(3)
        self.assertTrue(ll.search(1))
        ll.delete(1)
        self.assertFalse(ll.search(1))
        self.assertTrue(ll.search(2))
        self.assertTrue(ll.search(3))

    # attempt to delete a value that doesn't exist in a list (shouldn't crash)
    def test_delete_missing(self):
        ll = LinkedList()
        ll.insert(10)
        ll.delete(15)

    # attempt to delete from an empty list (shouldn't crash)
    def test_delete_empty(self):
        ll = LinkedList()
        ll.delete(5)

if __name__ == "__main__":
    unittest.main()