import unittest
from Python_assessment.src.assignment11.util import check

class MyTestCase(unittest.TestCase):
    def test_something(self):
        email = 'pritirai326@gmail.com'  # Define the email variable
        self.assertEqual(check(email), 'pritirai326@gmail.com')  # Correct comparison

if __name__ == '__main__':
    unittest.main()


