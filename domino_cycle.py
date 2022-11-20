"""
Proposed solution for the domino_cycle problem from 109 Python Problems for CCPS
"""


def domino_cycle(tiles):
    """
    Checks if a list of tuples statisfies a domino cycle.
    :parameter tiles (list of 2-tuples)
    :return boolean
    """
    if len(tiles) > 1:
        for index, tile in enumerate(tiles):
            if tile[1] != tiles[index + 1][0]:
                return False
            if index == len(tiles) - 2:
                break
    if not tiles:
        return True
    if tiles[-1][1] != tiles[0][0]:
        return False
    return True
