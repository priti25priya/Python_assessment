import unittest
from Python_assessment.src.assignment5.util import StringFormat


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result=5
        self.assertEqual(StringFormat(result),None) # add assertion here


if __name__ == '__main__':
    unittest.main()
