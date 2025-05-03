import calculator
from data_structures import Date
import unittest
from unittest.mock import patch

class TestCalculator(unittest.TestCase):
    def test_calculate_lucky_number(self):
        birthday = [(10, 3, 2006), (6, 6, 2017)]
        
        expected = [3, 22]
        
        msg = [
            "Case: Not master number",
            "Case: Master number"]
    
        for i in range(len(expected)):
            with patch('builtins.input', side_effect=[str(x) for x in birthday[i]]):
                test_date = Date()
                test_date.prompt_date()
                self.assertEqual(expected[i], calculator.calculate_lucky_number(test_date), msg[i])

    def test_get_lucky_animal(self):
        lucky_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 0]
        expected = [
            "Parrot",
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


    def test_get_generation_bva(self):
        year_lower = [1945, 1964, 1979, 1994, 2009]
        year_upper = [1946, 1965, 1980, 1995, 2010]
        expected_lower = [
            "Silent Generation",
            "Baby Boomers",
            "Generation X",
            "Millennials",
            "Generation Z"]
        
        expected_upper = [
            "Baby Boomers",
            "Generation X",
            "Millennials",
            "Generation Z",
            "Generation Alpha"]

        msg = ["Silent Generation / Baby Boomers",
                    "Baby Boomers / Generation X",
                    "Generation X / Millennials",
                    "Millennials / Generation Z",
                    "Generation Z / Generation Alpha"]
        
        for i in range(len(expected_lower)):
            self.assertEqual(expected_lower[i], calculator.get_generation(year_lower[i]), f"[Lower] {msg[i]}")
            self.assertEqual(expected_upper[i], calculator.get_generation(year_upper[i]), f"[Upper] {msg[i]}")
