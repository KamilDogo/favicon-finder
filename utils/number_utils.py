def is_valid_number(number):
    try:
        return int(number) > 0
    except ValueError:
        return False
