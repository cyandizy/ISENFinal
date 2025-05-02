class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.year = year

        if isinstance(month, str):
            self.month = self.format_month(month)
        else:
            self.month = month

        if self.day not in range(1, 32):
            raise ValueError("Day value must be from 1 to 31 inclusive.")
        elif self.month not in range(1, 13):
            raise ValueError("Month value must be from 1 to 12 inclusive.")
        elif self.year not in range(1901, 2025):
            raise ValueError("Year value must be from 1901 to 2024 inclusive")

    def format_month(self, month: str):
        month = month.lower()
        month_dict = {
            "january": 1, "february": 2, "march": 3, "april": 4, "may": 5, "june": 6,
            "july": 7, "august": 8, "september": 9, "october": 10, "november": 11, "december": 12,
            "jan": 1, "feb": 2, "mar": 3, "apr": 4, "jun": 6, "jul": 7,
            "aug": 8, "sep": 9, "sept": 9, "oct": 10, "nov": 11, "dec": 12
        }
        if month not in month_dict.keys():
            raise ValueError

        return month_dict[month]
