import unittest
import io
import sys
from date import Date
import calculator

class TestWhitebox(unittest.TestCase):
    def test_calculate_lucky_number(self):
        birthday = [(10, 3, 2006), 
                    (6, 6, 2017)]
        
        expected = [3, 22]
        
        msg = [
            "Path: Do not enter if",
            "Path: Enter if"]
    
        for i in range(len(expected)):
            sys.stdin = io.StringIO(f"{birthday[i][0]}\n{birthday[i][1]}\n{birthday[i][2]}")
            date = Date()
            date.prompt_date()
            self.assertEqual(expected[i], calculator.calculate_lucky_number(date), msg[i])
    
    def test_prompt_date(self):
        date = [
            (10, "march", 2006),
            (44, "april", 2006),
            (14, "may", 200),
            (12, 9, 2004),
            (-1, 4, 2024),
            (4, 99, 1945),
            (9, 12, 2174)]
        
        expected = [
                (10, 3, 2006),
                ValueError,
                ValueError,
                (12, 9, 2004),
                ValueError,
                ValueError,
                ValueError]
        
        msg = [
            "Path 1: Enter first if, do not enter second if",
            "Path 2: Enter first if, enter second if",
            "Path 3: Enter 1st if, enter 2nd else of 2nd if",
            "Path 4: Enter else of 1st if, do not enter second if",
            "Path 5: Enter else of 1st if, enter 2nd if",
            "Path 6: Enter else of 1st if, enter 1st else of 2nd if",
            "Path 7: Enter else of 1st if, enter 2nd else of 2nd if",
        ]

        for i in range(len(expected)):
            if expected[i] == ValueError:
                with self.assertRaises(ValueError, msg=msg[i]):
                    sys.stdin = io.StringIO(f"{date[i][0]}\n{date[i][1]}\n{date[i][2]}")
                    test_date = Date()
                    test_date.prompt_date()
            else:      
                sys.stdin = io.StringIO(f"{date[i][0]}\n{date[i][1]}\n{date[i][2]}")
                test_date = Date()     
                test_date.prompt_date()         
                self.assertEqual(expected[i][0], test_date.day, msg[i])
                self.assertEqual(expected[i][1], test_date.month, msg[i])
                self.assertEqual(expected[i][2], test_date.year, msg[i])
