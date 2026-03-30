import unittest
from algorithms import merge_sort, binary_search

class TestAlgorithms(unittest.TestCase):

    # merge sort on an unsorted list
    def test_unsorted_merge(self):
        result = merge_sort([3, 5, 2, 1, 4])
        self.assertEqual(result, [1, 2, 3, 4, 5])

    # merge sort on an already sorted list (should not be changed)
    def test_presorted_merge(self):
        result = merge_sort([1, 2, 3, 4, 5])
        self.assertEqual(result, [1, 2, 3, 4, 5])

    # merge sort on a list containing only one element
    def test_single_item_merge(self):
        result = merge_sort([10])
        self.assertEqual(result, [10])

    # merge sort on an empty list
    def test_empty_merge(self):
        result = merge_sort([])
        self.assertEqual(result, [])

    # merge sort on a list with duplicate data
    def test_duplicate_merge(self):
        result = merge_sort([1, 4, 3, 1, 2, 3, 5, 5])
        self.assertEqual(result, [1, 1, 2, 3, 3, 4, 5, 5])

    # merge sort on a list containing negative values
    def test_negatives_merge(self):
        result = merge_sort([3, 2, -1, -3, 0])
        self.assertEqual(result, [-3, -1, 0, 2, 3])

    # binary search with value in the list
    def test_binary_search(self):
        result = binary_search([1, 2, 3, 4, 5], 3)
        self.assertTrue(result)

    # binary search with a value not in the list
    def test_missing_binary_search(self):
        result = binary_search([1, 2, 3, 4, 5], 6)
        self.assertFalse(result)

    # find the first value in a list using binary search
    def test_first_binary_search(self):
        result = binary_search([1, 2, 3, 4, 5], 1)
        self.assertTrue(result)

    # find the last value in a list using binary search
    def test_last_binary_search(self):
        result = binary_search([1, 2, 3, 4, 5], 5)
        self.assertTrue(result)

    # test binary search on the output of a merge sort
    def test_merge_sort_binary_search(self):
        result = binary_search(merge_sort([4, 5, 1, 3, 2]), 3)
        self.assertTrue(result)