import unittest
from Python_assessment.src.assignment14.util import find_unique_numbers


class MyTestCase(unittest.TestCase):
    def test_something(self):
        my_list = [1, 2, 3, 4, 5, 3, 2, 1, 6, 7]
        result=[1,2,3,4,5,6,7]
        self.assertEqual(find_unique_numbers(my_list), result)  # add assertion here


if __name__ == '__main__':
    unittest.main()
