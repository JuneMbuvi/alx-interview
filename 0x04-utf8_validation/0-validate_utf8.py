#!/usr/bin/python3
"""method that determines if a given
data set represents a valid UTF-8 encoding"""


def validUTF8(data):
    """Returns True if data is a valid UTF-8 encoding, else return False"""
    i = 0
    while i < len(data):
        leading_ones = 0
        mask = 1 << 7
        while mask & data[i]:
            leading_ones += 1
            mask >>= 1
        if leading_ones == 0:
            i += 1
            continue
        if leading_ones == 1 or leading_ones > 4:
            return False
        trailing_bytes = leading_ones - 1
        i += 1
        while trailing_bytes > 0:
            if i >= len(data) or (data[i] >> 6) != 0b10:
                return False
            i += 1
            trailing_bytes -= 1
    return True
