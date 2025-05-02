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
            "Case: Day = 1-31, Month = 1-12, Year = 1901-2024 (all inclusive)",
            "Case: String month",
            "Case: Invalid day",
            "Case: Invalid month",
            "Case: Invalid year",
            "Case: Invalid day and month",
            "Case: Invalid month and year",
            "Case: Invalid day and year",
            "Case: Invalid day, month, and year"
        ]

        for i in range(len(expected)):
            if expected[i] == ValueError:
                with self.assertRaises(ValueError, msg=msg[i]):
                    data_structures.Date(*dates[i])
            else:
                self.assertEqual(expected[i], data_structures.Date(*dates[i]), msg[i])

    def test_format_month(self):
        test_date = data_structures.Date(1, 4, 2012)
        month = [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December",
            "Jan", "Feb", "Mar", "Apr", "Jun", "Jul",
            "Aug", "Sep", "Sept", "Oct", "Nov", "Dec",
            "jan", "JAN", "Jupiter"
        ]

        expected = [
            1, 2, 3, 4, 5, 6,
            7, 8, 9, 10, 11, 12,
            1, 2, 3, 4, 6, 7,
            8, 9, 9, 10, 11, 12,
            1, 1, ValueError
        ]

        msg = [
            "Case: January", 
            "Case: February", 
            "Case: March", 
            "Case: April", 
            "Case: May", 
            "Case: June",
            "Case: July", 
            "Case: August", 
            "Case: September", 
            "Case: October", 
            "Case: November", 
            "Case: December",
            "Case: Jan", 
            "Case: Feb", 
            "Case: Mar", 
            "Case: Apr", 
            "Case: Jun", 
            "Case: Jul",
            "Case: Aug", 
            "Case: Sep", 
            "Case: Sept", 
            "Case: Oct", 
            "Case: Nov", 
            "Case: Dec", 
            "Case: All lowercase",
            "Case: All upper case", 
            "Case: String does not match any month"
        ]

        for i in range(len(expected)):
            if expected[i] == ValueError:
                with self.assertRaises(ValueError, msg=msg[i]):
                    test_date.format_month(month[i])

            else:
                self.assertEqual(expected[i], test_date.format_month(month[i]), msg[i])
