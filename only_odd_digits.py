"""
Proposed solution for the only_odd_digits problem from 109 Python Problems for CCPS
"""


# Solution 1, attempt at single return statement solution
def only_odd_digits(number):
    """
    Checks if number only contains odd digits
    :param number
    :return boolean
    """
    return not any(bool(int(digit) % 2 == 0) for digit in list(str(number)))

# Solution 2, easy to read for-loop solution
def only_odds_digits(number):
    """
    Checks if number only contains odd digits
    :param number
    :return boolean
    """
    even_digits = [0, 2, 4, 6, 8]
    for digit in list(str(number)):
        if int(digit) in even_digits:
            return False
    return True
