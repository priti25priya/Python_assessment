import unittest
from Python_assessment.src.assignment13.util import find_max_and_min

class MyTestCase(unittest.TestCase):
    def test_something(self):
        x, y = 3, 3
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        # The min values per row are [1, 4, 7], so the max of these is 7
        self.assertEqual(find_max_and_min(x, y, matrix), 7)
        x, y = 2, 2
        matrix = [
            [10, 12],
            [5, 15]
        ]
        # The min values per row are [10, 5], so the max of these is 10
        self.assertEqual(find_max_and_min(x, y, matrix), 10)

        # Test case 3: 4x4 matrix with some negative values
        x, y = 4, 4
        matrix = [
            [-1, -2, -3, -4],
            [4, 5, 6, 7],
            [0, -1, 2, 3],
            [10, 11, 12, 13]
        ]
        # The min values per row are [-4, 4, -1, 10], and the max is 10
        self.assertEqual(find_max_and_min(x, y, matrix), 10)



if __name__ == '__main__':
    unittest.main()
