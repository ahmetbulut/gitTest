import unittest
from sorting import mock

class MyTestCase(unittest.TestCase):
    def test_sorting_1(self):
        self.assertEqual(None, mock())  # add assertion here

    def test_sorting_2(self):
        self.assertEqual(None, mock())  # add assertion here

    def test_IdontWannaFollowAnyConventions(self):
        #complicated X
        #complicated Y
        #...
        #if something is not right:
        raise AssertionError("Hello World!")
        #else:
        #pass

if __name__ == '__main__':
    unittest.main()
