import logic
from data_structures import Date
import unittest
import io
import sys

class TestLogic(unittest.TestCase):
    def test_same_luck(self):
        birthday1 = [(9, 7, 2005),
                     (9, 7, 2005)]
        
        birthday2 = [(8, 8, 2005),
                     (8, 9, 2005)]
        
        expected = [True, False]

        msg = ["Case: Lucky number of birthday1 == lucky number of birthday 2",
               "Case: Lucky number of birthday1 != equal to lucky number of birthday 2"]
        
        for i in range(len(expected)):
            date1 = Date()
            sys.stdin = io.StringIO(f"{birthday1[i][0]}\n{birthday1[i][1]}\n{birthday1[i][2]}")
            date1.prompt_date()
            date2 = Date()
            sys.stdin = io.StringIO(f"{birthday2[i][0]}\n{birthday2[i][1]}\n{birthday2[i][2]}")
            date2.prompt_date()
            result = logic.same_luck(date1, date2)
            self.assertEqual(expected[i], result, msg[i])

    def test_is_master_number(self):
        lucky_number = [11, 22, 33, 20, 14, 43]
        expected = [True, True, True, False, False, False]
        msg = ["Case: Lucky number == 11",
               "Case: Lucky number == 22",
               "Case: Lucky number == 33",
               "Case: Lucky number != 11",
               "Case: Lucky number != 22",
               "Case: Lucky number != 33"]
        
        for i in range(len(expected)):
            self.assertEqual(expected[i], logic.is_master_number(lucky_number[i]), msg[i])
