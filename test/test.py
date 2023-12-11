import unittest
from sorting import mock

class MyTestCase(unittest.TestCase):
    def test_sorting_boolean(self):
        self.assertEqual(True, mock())  # add assertion here

    def test_sorting_none(self):
        self.assertEqual(None, mock())  # add assertion here

if __name__ == '__main__':
    unittest.main()
