from data_structures import Date
import logic

def calculate_lucky_number(birthday: Date):
    date_string = str(birthday.day) + str(birthday.month) + str(birthday.year)
    lucky_number = 0
    for char in date_string:
        lucky_number += int(char)
    if not logic.is_master_number(lucky_number):
        tmp_lucky_number = 0
        for char in str(lucky_number):
            tmp_lucky_number += int(char)
        lucky_number = tmp_lucky_number

    return lucky_number

def get_lucky_animal(lucky_number):
    lucky_animal_dict = {
        1: "Parrot",
        2: "Rabbit",
        3: "Elephant",
        4: "Beetles",
        5: "Bears",
        6: "Deer",
        7: "Crane",
        8: "Horse",
        9: "Fish",
        11: "Dolphin",
        22: "Lion",
        33: "Turtle"
    }
    if lucky_number in lucky_animal_dict.keys():
       return lucky_animal_dict[lucky_number]
    else:
        return "" 


def get_generation(year):
    ...