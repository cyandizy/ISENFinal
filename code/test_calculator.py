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
        
        msg = ["Case: Intended",
               "Case: Invalid day",
               "Case: Invalid month",
               "Case: Invalid year",
               "Case: Invalid day and month",
               "Case: Invalid month and year",
               "Case: Invalid day and year",
               "Case: Invalid day, month, and year"]
        
        for i in range(len(expected)):
            self.assertEqual(expected[i], calculator.calculate_lucky_number(birthday[i]), msg[i])

    def test_get_lucky_animal(self):
        lucky_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 0]
        expected = ["Parrot",
                    "Rabbit",
                    "Elephant",
                    "Beetles",
                    "Bears",
                    "Deer",
                    "Crane",
                    "Horse",
                    "Fish",
                    "Dolphin",
                    "Lion",
                    "Turtle", 
                    ""]
        
        msg = ["Case: Lucky number == 1",
               "Case: Lucky number == 2",
               "Case: Lucky number == 3",
               "Case: Lucky number == 4",
               "Case: Lucky number == 5",
               "Case: Lucky number == 6",
               "Case: Lucky number == 7",
               "Case: Lucky number == 8",
               "Case: Lucky number == 9",
               "Case: Lucky number == 11",
               "Case: Lucky number == 22",
               "Case: Lucky number == 33",
               "Case: Lucky number not in range 1-9 inclusive and not 11, 22, and 33"]
        
        for i in range(len(expected)):
            self.assertEqual(expected[i], calculator.get_lucky_animal(lucky_number[i]), msg[i])
    
    def test_get_generation(self):
        year = [1930, 1950, 1970, 1990, 2000, 2020]
        expected = ["Silent Generation",
                    "Baby Boomers",
                    "Generation X",
                    "Millennials",
                    "Generation Z",
                    "Generation Alpha"]
        
        msg = ["Case: 1901 <= year <= 1945",
               "Case: 1946 <= year <= 1964",
               "Case: 1965 <= year <= 1979",
               "Case: 1980 <= year <= 1994",
               "Case: 1995 <= year <= 2009",
               "Case: 2010 <= year <= 2024"]
        
        for i in range(len(expected)):
            self.assertEqual(expected[i], calculator.get_generation(year[i]), msg[i])