import calculator
from data_structures import Date
import unittest

class TestCalculator(unittest.TestCase):
    def test_calculate_lucky_number(self):
        birthday = [Date(10, 3, 2006),
                    Date(0, 2, 2001),
                    Date(10, 0, 1999),
                    Date(20, 4, 9999),
                    Date(-1, 0, 2004),
                    Date(4, 99, 2193),
                    Date(111, 12, 9),
                    Date(99, 99, 9999)]
        
        expected = [12,
               ValueError,
               ValueError,
               ValueError,
               ValueError,
               ValueError,
               ValueError,
               ValueError]
        
        msg = ["Intended Case",
               "Invalid day",
               "Invalid month",
               "Invalid year",
               "Invalid day and month",
               "Invalid month and year",
               "Invalid day and year",
               "Invalid day, month, and year"]
        
        for i in range(len(expected)):
            self.assertEqual(expected[i], calculator.calculate_lucky_number(birthday[i]), msg[i])