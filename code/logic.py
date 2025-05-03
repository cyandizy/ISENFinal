import calculator

def same_luck():
    lucky_number1 = calculator.calculate_lucky_number()
    lucky_number2 = calculator.calculate_lucky_number()
    if (lucky_number1 == lucky_number2):
        return True
    else:
        return False

def is_master_number(lucky_number):
    if lucky_number in [11, 22, 33]:
        return True
    else:
        return False