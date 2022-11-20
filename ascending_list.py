"""
Proposed solution for the ascending_list problem from 109 Python Problems for CCPS
"""


def is_ascending(items):
    """Checks if a list is strictly ascending"""
    for counter, item in enumerate(items):
        if counter == len(items) - 1:
            break
        if item >= items[counter + 1]:
            return False
    return True
