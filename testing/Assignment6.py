import unittest
from Python_assessment.src.assignment6.util import datetime


class MyTestCase(unittest.TestCase):
    def test_something(self):
        # Split the string into day, month, and year integers
        date_str = "25 12 2018"
        day, month, year = map(int, date_str.split())

        # Create a datetime object
        date_obj = datetime(year, month, day)

        # Get the name of the day of the week (Tuesday in this case)
        weekday = date_obj.strftime("%A")

        # Compare the result with the expected day of the week
        self.assertEqual(weekday, "Tuesday")


if __name__ == '__main__':
    unittest.main()
