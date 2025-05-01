import logic
from data_structures import Date
import unittest

class TestLogic(unittest.TestCase):
    def test_same_luck(self):
        birthday1 = [Date(9, 7, 2005),
                     Date(9, 7, 2005)]
        
        birthday2 = [Date(8, 8, 2005),
                     Date(8, 9, 2005)]
        
        expected = [True, False]

        msg = ["Case: Lucky number of birthday1 == lucky number of birthday 2",
               "Case: Lucky number of birthday1 != equal to lucky number of birthday 2"]
        
        for i in range(len(expected)):
            self.assertEqual(expected[i], logic.same_luck(birthday1[i], birthday2[i]), msg[i])

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
            self.assertEqual(expected[i], logic.same_luck(lucky_number[i]), msg[i])
