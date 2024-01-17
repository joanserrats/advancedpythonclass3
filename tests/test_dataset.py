"""
test loading of the dataset
"""

import unittest
from scripts.repo_first_script import load_dataset


class TestDataset(unittest.TestCase):
    """
    class to test the dataset input in different ways
    """
    
    def setUp(self):
        """
        path to dataset
        """
        self.path = "dataset/BooksDatasetClean.csv"


def test_extension_fail(self):
    """
    test for the extension of the dataset
    """
    with self.assertRauses(ValueError):
        load_dataset(self.path)


