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
        
        if isinstance(self.month, str):
            self.month = self.format_month(self.month)

    def format_month(self):
        month_dict = {
            "January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6,
            "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12,
            "Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "Jun": 6, "Jul": 7,
            "Aug": 8, "Sep": 9, "Sept": 9, "Oct": 10, "Nov": 11, "Dec": 12
        }
        return month_dict[self.month]
