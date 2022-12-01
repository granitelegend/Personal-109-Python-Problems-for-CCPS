"""
Proposed solution for the ascending_list problem from 109 Python Problems for CCPS
"""


# Solution 1, single return statement solution.
def is_ascending(items):
    return not any([True for x, y in zip(items, items[1:]) if x >= y])


# Solution 2, for-loop + try-except solution
def is_ascending(items):
    for index, item in enumerate(items):
        try:
            if item >= items[index + 1]:
                return False
        except IndexError:
            break
    return True
