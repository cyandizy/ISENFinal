import data_structures
import unittest

class TestDate(unittest.TestCase):
    def test_constructor(self):
        dates = [
            (10, 3, 2006),
            (10, "March", 2006),
            (0, 2, 2001),
            (10, 0, 1999),
            (20, 4, 9999),
            (-1, 0, 2004),
            (4, 99, 2193),
            (111, 12, 9),
            (99, 99, 9999)]
        
        expected = [
                None,
                None,
                ValueError,
                ValueError,
                ValueError,
                ValueError,
                ValueError,
                ValueError,
                ValueError]
        
        msg = [
            "Day = 1-31, Month = 1-12, Year = 1901-2024 (all inclusive)",
            "String month",
            "Invalid day",
            "Invalid month",
            "Invalid year",
            "Invalid day and month",
            "Invalid month and year",
            "Invalid day and year",
            "Invalid day, month, and year"
        ]

        for i in range(len(expected)):
            if expected[i] == ValueError:
                self.assertRaises(expected[i], data_structures.Date(*dates[i]), msg[i])
            else:
                self.assertEqual(expected[i], data_structures.Date(*dates[i]), msg[i])

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
