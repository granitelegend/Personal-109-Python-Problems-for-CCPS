"""
Proposed solution for the beat_the_previous problem from 109 Python Problems for CCPS
"""


def extract_increasing(digits):
    results, previous_number, current_number = [], -1, 0
    for d in digits:
        current_number = 10 * current_number + int(d)
        if previous_number < current_number:
            results.append(current_number)
            previous_number, current_number = current_number, 0
    return results
