import calculator
import logic
from data_structures import Date

def prompt_date(prompt_message):
    print(prompt_message)
    valid_input = False
    while not valid_input:
        day = input("Input day (integer)> ")
        month: str = input("Input month (integer or string)> ")
        year = input("Input year (string)> ")
        
        try:
            day = int(day)
            if month.isdigit():
                month = int(month)
            year = int(year)

            date = Date(day, month, year)
            valid_input = True

        except ValueError as e:
            print(f"One of the input was invalid, please try again... {e}")
    return date

if __name__ == "__main__":
    welcome_message = """
                        Which functionality would you like to use?
                        A: Find your lucky number, lucky animal, 
                        and whether your lucky number is a master number or not.
                        B: Check if two birthdays have the same lucky number and animal.
                        C: Check which generation you are in.
    """
    print(welcome_message)
    valid_input = False
    while not valid_input:
        input_scenario = input("Functionality A/B/C> ")
        if input_scenario[0].upper() == "A":
            birthday = prompt_date("Please enter your birthday.")
            generation = calculator.get_generation(birthday.year)
            print(f"You belong to {generation}.")
            print()
            lucky_number = calculator.calculate_lucky_number(birthday)
            if logic.is_master_number(lucky_number):
                print("Congratuation! Your lucky number is a master number!")
            lucky_animal = calculator.get_lucky_animal(lucky_number)
            print()
            print(f"Your lucky number is {lucky_number},")
            print(f"and animal is {lucky_animal}.")

            valid_input = True
        
        elif input_scenario[0].upper() == "B":
            birthday1 = prompt_date("Please enter birthday 1.")
            print()
            birthday2 = prompt_date("Please enter birthday 2.")
            if logic.same_luck(birthday1, birthday2):
                number = calculator.calculate_lucky_number(birthday1)
                animal = calculator.get_lucky_animal(birthday1)
                print(f"Two birthdays have the same luck! You both have number {number} and {animal}")
            else:
                print("Unfortunately, two birthdays do not have the same luck.")

            valid_input = True

        elif input_scenario[0].upper() == "C":
            birthday = prompt_date("Please enter your birthday.")
            generation = calculator.get_generation(birthday.year)
            print(f"You belong to {generation}.")

            valid_input = True
        
        if not valid_input:
            print("Your input is invalid, please try again.")
