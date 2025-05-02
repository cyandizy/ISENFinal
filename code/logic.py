import calculator

def same_luck(birthday1, birthday2):
    if (calculator.calculate_lucky_number(birthday1) ==
        calculator.calculate_lucky_number(birthday2)):
        return True
    else:
        return False

def is_master_number(lucky_number):
    if lucky_number in [11, 22, 33]:
        return True
    else:
        return False