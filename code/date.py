class Date:
    """
        Stores day, month, year in integer format.
    """

    def __init__(self):
        self.day = None
        self.month = None
        self.year = None

    def prompt_date(self):
        """
            Prompts for user input for day, month, and year, 
            validifies if they are in correct formats and calls format_month to format month if month is not a digit. 
            Finally, it modifies class members day, month, year with new values.
        """

        day = input("Input day (integer)> ")
        month = input("Input month (integer or string)> ")
        year = input("Input year (string)> ")
        day = int(day)
        year = int(year)

        if not month.isdigit():
            month = self.format_month(month)
        else:
            month = int(month)

        if day not in range(1, 32):
            raise ValueError("Day value must be from 1 to 31 inclusive.")
        elif month not in range(1, 13):
            raise ValueError("Month value must be from 1 to 12 inclusive.")
        elif year not in range(1901, 2025):
            raise ValueError("Year value must be from 1901 to 2024 inclusive")
                
        self.day = day
        self.month = month
        self.year = year

    def format_month(self, month: str):
        """
            Formats month to integer by using a dictionary 
            that maps month strings to integers and return the integer. 
        """
        
        month = month.lower()
        month_dict = {
            "january": 1, "february": 2, "march": 3, "april": 4, "may": 5, "june": 6,
            "july": 7, "august": 8, "september": 9, "october": 10, "november": 11, "december": 12,
            "jan": 1, "feb": 2, "mar": 3, "apr": 4, "jun": 6, "jul": 7,
            "aug": 8, "sep": 9, "sept": 9, "oct": 10, "nov": 11, "dec": 12
        }
        if month not in month_dict.keys():
            raise ValueError(f"{month} is not a month.")

        return month_dict[month]
