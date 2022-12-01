"""
Proposed solution for the ascending_list problem from 109 Python Problems for CCPS
"""


def is_ascending(items):
    for index, item in enumerate(items):
        try:
            if item >= items[index + 1]:
                return False
        except IndexError:
            break
    return True