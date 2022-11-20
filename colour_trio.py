"""
Proposed solution for the cyclops_numbers problem from 109 Python Problems for CCPS
Note: 'brrrrr' -> 'y' and 'rybyry' -> 'r'
Yet following the same process used for 'brrrrr', makes 'rybyry' become 'b'.
This is wrong since the expected result is 'r'. Either I am wrong -
- or there must be a mistake in the .pdf.
"""


def colour_trio(colours):
    """Reduces string of colours to a single colour"""
    colour_conversion_dict = {
        # Create Blue
        'ry': 'b',
        'yr': 'b',
        'bb': 'b',
        # Create Red
        'yb': 'r',
        'by': 'r',
        'rr': 'r',
        # Create Yellow
        'br': 'y',
        'rb': 'y',
        'yy': 'y',
    }
    while len(colours) != 1:
        colour = colours[:2]
        colours = colours[2:]
        colours = colour_conversion_dict[colour] + colours
    return colours
