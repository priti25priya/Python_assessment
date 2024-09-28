import unittest
from Python_assessment.src.assignment10.util import CountWord


class MyTestCase(unittest.TestCase):
    def test_something(self):
        Fruits = ['apple', 'orange', 'apple', 'orange', 'cherry', 'apple']
        word = 'apple'
        self.assertEqual(CountWord(Fruits,word),3 )  # add assertion here


if __name__ == '__main__':
    unittest.main()
