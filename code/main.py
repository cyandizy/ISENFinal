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
            try:
                birthday = Date()
                birthday.prompt_date()
            except Exception as e:
                print(f"\nError: {e}\n")
                print("Please try again...")
                continue

            generation = calculator.get_generation(birthday.year)
            print()
            print(f"You belong to {generation}.")
            lucky_number = calculator.calculate_lucky_number(birthday)
            if logic.is_master_number(lucky_number):
                print("Congratuations! Your lucky number is a master number!")
            lucky_animal = calculator.get_lucky_animal(lucky_number)
            print()
            print(f"Your lucky number is {lucky_number},")
            print(f"and animal is {lucky_animal}.")

            break
        
        elif choice == "B":
            try:
                birthday1 = Date()
                birthday2 = Date()
                print("Please enter birthday 1.")
                birthday1.prompt_date()
                print("Please enter birthday 2.")
                birthday2.prompt_date()
            except Exception as e:
                print(f"\nError: {e}\n")
                print("Please try again...")
                continue

            if logic.same_luck(birthday1, birthday2):
                number = calculator.calculate_lucky_number(birthday1)
                animal = calculator.get_lucky_animal(number)
                print(f"\nTwo birthdays have the same luck! You both have number {number} and {animal}\n")
            else:
                print("\nUnfortunately, two birthdays do not have the same luck.\n")

            break

        elif choice == "C":
            print("Please enter your birthday.")
            try:
                birthday = Date()
                birthday.prompt_date()
            except Exception as e:
                print(f"\nError: {e}\n")
                print("Please try again...")
                continue
            
            generation = calculator.get_generation(birthday.year)
            print(f"\nYou belong to {generation}.\n")

            break
        
        if not valid_input:
            print("Your input is invalid, please try again.")
