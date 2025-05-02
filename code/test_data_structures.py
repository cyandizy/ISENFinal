import data_structures
import unittest

class TestDate(unittest.TestCase):
    def test_format_month(self):
        month = [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December",
            "Jan", "Feb", "Mar", "Apr", "Jun", "Jul",
            "Aug", "Sep", "Sept", "Oct", "Nov", "Dec"
        ]

        expected = [
            1, 2, 3, 4, 5, 6,
            7, 8, 9, 10, 11, 12,
            1, 2, 3, 4, 6, 7,
            8, 9, 9, 10, 11, 12
        ]

        msg = [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December",
            "Jan", "Feb", "Mar", "Apr", "Jun", "Jul",
            "Aug", "Sep", "Sept", "Oct", "Nov", "Dec"
        ]

        for i in range(len(expected)):
            self.assertEqual(expected[i], data_structures.Date.format_month(month[i]), msg[i])
