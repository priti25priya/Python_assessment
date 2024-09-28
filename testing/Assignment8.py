import datetime
import unittest
from Python_assessment.src.assignment8.util import Time_delta


class MyTestCase(unittest.TestCase):
    def test_something(self):
        # Assuming Time_delta() should return a timedelta of 2 hours
        expected_delta = datetime.timedelta(hours=2)
        self.assertEqual(Time_delta(), expected_delta)  # Compare with 2-hour timedelta


#if __name__ == '__main__':
    # unittest.main()
