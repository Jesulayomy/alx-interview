#!/usr/bin/python3
""" This module validates a stream of utf8 data """
from typing import List


def validUTF8(data: List[int]):
    """
        Confirms if a set of data is a valid utf8 encoding
        Returns True if valid or false if nolt valid
    """

    for byte in data:
        if byte > 255 or type(byte) != int or byte < 0:
            return False

    return True
