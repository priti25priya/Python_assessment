import unittest
import numpy as np
from Python_assessment.src.assignment9. util import CalculateFloorCeilRint
class TestCalculateFloorCeilRint(unittest.TestCase):
    def test_CalculateFloorCeilRint(self):
        input_data = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9]
        expected_output = [
            (np.floor(1.1), np.ceil(1.1), np.rint(1.1)),
            (np.floor(2.2), np.ceil(2.2), np.rint(2.2)),
            (np.floor(3.3), np.ceil(3.3), np.rint(3.3)),
            (np.floor(4.4), np.ceil(4.4), np.rint(4.4)),
            (np.floor(5.5), np.ceil(5.5), np.rint(5.5)),
            (np.floor(6.6), np.ceil(6.6), np.rint(6.6)),
            (np.floor(7.7), np.ceil(7.7), np.rint(7.7)),
            (np.floor(8.8), np.ceil(8.8), np.rint(8.8)),
            (np.floor(9.9), np.ceil(9.9), np.rint(9.9)),
        ]
        result = CalculateFloorCeilRint(input_data)
        for res, exp in zip(result, expected_output):
            self.assertTrue(np.allclose(res, exp))

if __name__ == '__main__':
    unittest.main()
