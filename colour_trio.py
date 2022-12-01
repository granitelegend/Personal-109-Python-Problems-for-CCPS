"""
Proposed solution for the cyclops_numbers problem from 109 Python Problems for CCPS
"""


def colour_trio(colours):
    """Reduces string of colours to a single colour"""
    colour_conversion_dict = {'ry': 'b', 'yr': 'b',
                              'bb': 'b', 'yb': 'r',
                              'by': 'r', 'rr': 'r',
                              'br': 'y', 'rb': 'y',
                              'yy': 'y',
                              }
    while len(colours) != 1:
        current_colours = ''
        for index in range(len(colours)):
            current_colours = current_colours + colour_conversion_dict[colours[index:index + 2]]
            if index == len(colours) - 2:
                break
        colours = current_colours[:]
    return colours
