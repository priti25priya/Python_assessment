import unittest
from Python_assessment.src.assignment12.util import Sets


class MyTestCase(unittest.TestCase):
    def test_something(self):
        sub=[1, 2, 3 ,4 ,5]
        A={1 ,2, 3}
        B={2 ,3, 4}
        self.assertEqual(Sets(sub,A,B), 2)  # add assertion here


if __name__ == '__main__':
    unittest.main()
