# || START LECTURE NOTES ||
# Simple unit test case for loading the data
# || END LECTURE NOTES ||


import sys
import os
import unittest

# Add the parent directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Now import from ml_code
from ml_code.data_load import load_data


class TestDataLoad(unittest.TestCase):
    def test_load_data(self):
        # Test loading data from a valid file path
        data = load_data("../data/data.csv")
        self.assertIsNotNone(data)
        self.assertTrue(len(data) > 0)

    def test_load_data_invalid_path(self):
        # Test loading data from an invalid file path
        data = load_data("invalid_path.csv")
        self.assertIsNone(data)
