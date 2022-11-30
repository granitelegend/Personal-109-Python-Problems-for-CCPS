"""
Proposed solution for the count_dominators problem from 109 Python Problems for CCPS
"""


def count_dominators(numbers):
    dominator_count, current_number = 0, 0
    if numbers:
        numbers.reverse()
        dominator_count, current_number = 1, numbers[0]
    for number in numbers:
        if current_number < number:
            current_number = number
            dominator_count += 1
    return dominator_count
