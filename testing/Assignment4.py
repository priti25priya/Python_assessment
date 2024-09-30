import unittest
from Python_assessment.src.assignment4.util import merge

class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = merge("MANAGERIO", 3)

        # Assuming the function is expected to return None
        self.assertEqual(result, None)  # Change the expected result to None


if __name__ == '__main__':
    unittest.main()
