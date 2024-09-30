import unittest
from Python_assessment.src.assignment3.util import modify_string

class MyTestCase(unittest.TestCase):
    def test_something(self):
        result="dummy"
        self.assertEqual(modify_string(), result)  # add assertion here


if __name__ == '__main__':
    unittest.main()
