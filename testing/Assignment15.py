import unittest
from Python_assessment.src.assignment15.util import count_words, count_characters

class MyTestCase(unittest.TestCase):

    def test_count_words(self):
        # Test cases for count_words function
        self.assertEqual(count_words("This is a simple test."), 5)

    def test_count_characters(self):
        # Test cases for count_characters function
        self.assertEqual(count_characters("This is a simple test."), 17)  # Simple sentence




if __name__ == '__main__':
    unittest.main()
