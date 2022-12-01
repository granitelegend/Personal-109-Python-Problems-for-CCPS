"""
Proposed solution for the iterated_ordinal_transform problem from 109 Python Problems for CCPS
"""


def ordinal_transform(seed, i):
    while len(seed) <= i:
        ordinal_count, ordinal_list = {}, []
        for number in seed:
            ordinal_count.setdefault(number, 0)
            ordinal_count[number] += 1
            ordinal_list.append(ordinal_count[number])
        seed = seed + ordinal_list
    return seed[i]
