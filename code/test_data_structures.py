from data_structures import *
import unittest
import io
import sys

class TestDate(unittest.TestCase):
    def test_prompt_date(self):
        dates = [
            (10, 3, 2006),
            (10, "March", 2006),
            (0, 2, 2001),
            (10, 0, 1999),
            (20, 4, 5701),
            (-1, 0, 2004),
            (4, 99, 2193),
            (111, 12, 9),
            (99, 99, 5701)]
        
        expected = [
                (10, 3, 2006),
                (10, 3, 2006),
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
                    sys.stdin = io.StringIO(f"{dates[i][0]}\n{dates[i][1]}\n{dates[i][2]}")
                    test_date = Date()
                    test_date.prompt_date()
            else:      
                sys.stdin = io.StringIO(f"{dates[i][0]}\n{dates[i][1]}\n{dates[i][2]}")
                test_date = Date()     
                test_date.prompt_date()         
                self.assertEqual(expected[i][0], test_date.day, msg[i])
                self.assertEqual(expected[i][1], test_date.month, msg[i])
                self.assertEqual(expected[i][2], test_date.year, msg[i])

    def test_format_month(self):
        sys.stdin = io.StringIO("1\n4\n2006")
        test_date = Date()
        test_date.prompt_date()

        month = [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December",
            "Jan", "Feb", "Mar", "Apr", "Jun", "Jul",
            "Aug", "Sep", "Sept", "Oct", "Nov", "Dec",
            "jan", "JAN", "Pispol"
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
