class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
        if self.day not in range(1, 32):
            return ValueError("Day value must be from 1 to 31 inclusive.")
        elif self.month not in range(1, 13):
            return ValueError("Month value must be from 1 to 12 inclusive.")
        elif self.year not in range(1901, 2025):
            return ValueError("Year value must be from 1901 to 2024 inclusive")