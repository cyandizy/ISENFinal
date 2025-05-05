import calculator

def same_luck(birthday1, birthday2):
    """
        Checks if two dates have the same lucky number and lucky animal 
        by receiving birthday1 and birthday2 as arguments, 
        then call calculate_lucky_number for each birthday and compare the results. 
        It returns True if both have the same lucky number, and False if not.
    """

    if (calculator.calculate_lucky_number(birthday1) ==
        calculator.calculate_lucky_number(birthday2)):
        return True
    else:
        return False

def is_master_number(lucky_number):
    """
        Checks if a lucky number is a master number by receiving lucky number as argument 
        and check if the number is in the list of master numbers of not. 
        If it is in the list, return True. If it is not, return False.
    """


    if lucky_number in [11, 22, 33]:
        return True
    else:
        return False