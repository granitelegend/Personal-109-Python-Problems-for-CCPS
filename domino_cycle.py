"""
Proposed solution for the domino_cycle problem from 109 Python Problems for CCPS
"""


def domino_cycle(tiles):
    if tiles:
        for index, tile in enumerate(tiles):
            try:
                if tiles[-1][1] != tiles[0][0] or tile[1] != tiles[index + 1][0]:
                    return False
            except IndexError:
                break
    return True
