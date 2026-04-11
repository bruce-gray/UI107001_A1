import unittest
from bst import BST
import random

class TestBST(unittest.TestCase):

    # tests regular inserts
    def test_insert(self):
        bst = BST()
        bst.insert(10)
        bst.insert(7)
        bst.insert(15.5)
        bst.insert(-3)
        self.assertTrue(bst.search(10))
        self.assertTrue(bst.search(7))
        self.assertTrue(bst.search(15.5))
        self.assertTrue(bst.search(-3))

    # tests inserts of duplicate data
    def test_insert_duplicate(self):
        bst = BST()
        bst.insert(1)
        bst.insert(1)
        self.assertTrue(bst.search(1))

    # search for a value that exists in the tree
    def test_search(self):
        bst = BST()
        bst.insert(10)
        bst.insert(7)
        bst.insert(15.5)
        bst.insert(-3)
        self.assertTrue(bst.search(7))

    # search for a value that does not exist in the tree
    def test_search_missing(self):
        bst = BST()
        bst.insert(5)
        self.assertFalse(bst.search(7))

    # search on an empty tree
    def test_search_empty(self):
        bst = BST()
        self.assertFalse(bst.search(7))

    # search on a tree with a degenerate data set (sequential)
    def test_search_degenerate(self):
        bst = BST()
        bst.insert(1)
        bst.insert(2)
        bst.insert(3)
        bst.insert(4)
        bst.insert(5)
        self.assertTrue(bst.search(1))
        self.assertTrue(bst.search(2))
        self.assertTrue(bst.search(3))
        self.assertTrue(bst.search(4))
        self.assertTrue(bst.search(5))

    # delete a regular leaf node and verify it's gone
    def test_delete_leaf(self):
        bst = BST()
        bst.insert(1)
        bst.insert(2)
        self.assertTrue(bst.search(2))
        bst.delete(2)
        self.assertFalse(bst.search(2))

    # delete a node with one child and verify it's gone but its child remains
    def test_delete_one_child(self):
        bst = BST()
        bst.insert(1)
        bst.insert(3)
        bst.insert(2)
        self.assertTrue(bst.search(3))
        self.assertTrue(bst.search(2))
        bst.delete(3)
        self.assertFalse(bst.search(3))
        self.assertTrue(bst.search(2))

    # delete a node with two children and verify it's gone but its children remain
    def test_delete_two_children(self):
        bst = BST()
        bst.insert(5)
        bst.insert(3)
        bst.insert(2)
        bst.insert(4)
        self.assertTrue(bst.search(3))
        self.assertTrue(bst.search(2))
        self.assertTrue(bst.search(4))
        bst.delete(3)
        self.assertFalse(bst.search(3))
        self.assertTrue(bst.search(2))
        self.assertTrue(bst.search(4))

    # delete the root node
    def test_delete_root(self):
        bst = BST()
        bst.insert(5)
        bst.insert(3)
        bst.insert(7)
        bst.delete(5)
        self.assertFalse(bst.search(5))
        self.assertTrue(bst.search(3))
        self.assertTrue(bst.search(7))

    # delete a non-existent value
    def test_delete_missing(self):
        bst = BST()
        bst.insert(10)
        bst.insert(20)
        self.assertFalse(bst.search(30))
        bst.delete(30)

    # attempt to delete from an empty tree
    def test_delete_empty(self):
        bst = BST()
        self.assertFalse(bst.search(1))
        bst.delete(1)

    # insert and search with a large randomised data set
    def test_large_dataset_search(self):
        bst = BST()
        randomised_list = [random.randint(0,9999) for _ in range(10000)]
        for i in randomised_list:
            bst.insert(i)
        self.assertTrue(bst.search(randomised_list[0])) # searching for the first randomly generated value

    # delete from a large randomised data set
    def test_large_dataset_delete(self):
        bst = BST()
        randomised_list = [random.randint(0,9999) for _ in range(10000)]
        for i in randomised_list:
            bst.insert(i)
        self.assertTrue(bst.search(randomised_list[0]))
        bst.delete(randomised_list[0])
        self.assertFalse(bst.search(randomised_list[0]))
