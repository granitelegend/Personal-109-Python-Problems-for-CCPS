"""
Proposed solution for the only_odd_digits problem from 109 Python Problems for CCPS
"""


def only_odds_digits(number):
    """
    Checks if number only contains even digits
    :param number
    :return boolean
    """
    even_digits = [0, 2, 4, 6, 8]
    for digit in list(str(number)):
        if int(digit) in even_digits:
            return False
    return True
