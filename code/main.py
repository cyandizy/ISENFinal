import calculator
import logic
from data_structures import Date

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
    while True:
        input_scenario = input("Functionality A/B/C> ").strip().upper()
        choice = input_scenario[0]
        if choice == "A":
            print("Please enter your birthday.")
            birthday = Date()
            generation = calculator.get_generation(birthday.year)
            print(f"You belong to {generation}.")
            print()
            lucky_number = calculator.calculate_lucky_number(birthday)
            if logic.is_master_number(lucky_number):
                print("Congratuations! Your lucky number is a master number!")
            lucky_animal = calculator.get_lucky_animal(lucky_number)
            print()
            print(f"Your lucky number is {lucky_number},")
            print(f"and animal is {lucky_animal}.")

            break
        
        elif choice == "B":
            print("Please enter birthday 1.")
            birthday1 = Date()
            print("Please enter birthday 2.")
            birthday2 = Date()
            if logic.same_luck(birthday1, birthday2):
                number = calculator.calculate_lucky_number(birthday1)
                animal = calculator.get_lucky_animal(number)
                print(f"Two birthdays have the same luck! You both have number {number} and {animal}")
            else:
                print("Unfortunately, two birthdays do not have the same luck.")

            break

        elif choice == "C":
            print("Please enter your birthday.")
            birthday = Date()
            generation = calculator.get_generation(birthday.year)
            print(f"You belong to {generation}.")

            break
        
        if not valid_input:
            print("Your input is invalid, please try again.")
