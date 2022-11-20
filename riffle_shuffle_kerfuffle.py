"""
Proposed solution for the riffle_shuffle_kerfuffle problem from 109 Python Problems for CCPS
"""


def riffle(items, out=True):
    """
    Performs the Faro shuffle on a even list.
    Unexecepted output if list is odd.
    """

    items_half_length = int(len(items) / 2)

    items_first_half = items[:items_half_length]
    items_second_half = items[items_half_length:]

    if out:
        for _ in range(items_half_length):
            items.append(items_first_half.pop(0))
            items.append(items_second_half.pop(0))
    else:
        for _ in range(items_half_length):
            items.append(items_second_half.pop(0))
            items.append(items_first_half.pop(0))

    items = items[int(len(items) / 2):]
    return items
