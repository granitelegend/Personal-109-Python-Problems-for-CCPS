"""
Proposed solution for the cyclops_numbers problem from 109 Python Problems for CCPS
"""

import math

# Solution 1, using import math, list and string type-casting and a single if-else block
def is_cyclops(number):
    """
    In order:
    Checks there is exactly one 0 in number.
    Checks if length of number is odd.
    Checks if the digit in the middle of number is 0.
    :param number (integer)
    :return boolean
    """
    if (
        list(str(number)).count("0") == 1
        and (int(math.log(number, 10)) + 1) % 2 != 0
        and list(str(number))[math.ceil(((int(math.log(number, 10)) + 1) / 2)) - 1]
        == "0"
        or number == 0
    ):
        return True
    return False


# Solution 2, using only loops, conditions and integer arithmetic operations
def number_length(number):
    """
    Returns number of digits in number
    :param number: int
    :return: int
    """
    counter = 0
    while number:
        counter += 1
        number //= 10
    return counter


def is_cyclops(number):
    """
    Checks if number is a cyclops number
    :param number:
    :return: boolean
    """

    if number_length(number) % 2 == 0 and number != 0:
        return False

    counter = 0
    zero_flag = 0
    half_number_length = int(number_length(number) / 2) + 1
    while number:
        counter += 1
        if number_length(number) == 1 and number != 0 and zero_flag != 1:
            return False
        if number % 10 != 0:
            number //= 10
        elif number % 10 == 0 and counter == half_number_length:
            number //= 10
            zero_flag += 1
        else:
            return False
    return True


# Solution 3, a shorter Solution 2 using Theorem 1.

# Unproven conjecture used as Theorem 1:
# The distance to before the middle of an odd list is k, k as solution to 2k+1 = len(List)
# Visual example of Theorem 1:
# [1,2,3,4,5,6,7,8,9], The middle number is 5.
# If I were to walk to 5 then I would have taken (n-1)/2 steps before stepping on 5.


def is_cyclops(n):
    mark_zero, count_length, count_zero = 0, 0, 0
    while True:
        count_length += 1
        if n % 10 == 0:
            mark_zero = count_length
            count_zero += 1
        n //= 10
        if not n:
            break
    return count_zero == 1 and mark_zero == ((count_length - 1) // 2) + 1


# Solution 4, an awful looking one-liner solution, assuming Theorem 1 is true.


def is_cyclops(n):
    return (
        int(list(str(n)).count("0")) == 1
        and int(list(str(n))[(len(str(n)) - 1) // 2]) == 0
    )
