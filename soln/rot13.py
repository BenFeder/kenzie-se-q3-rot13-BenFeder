#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Kenzie Assignment: rot13
"""

# Your name, plus anyone who helped you with this assignment.
# Give credit where credit is due.
__author__ = "pydan"

import sys
from string import ascii_lowercase, ascii_uppercase


def rotate(message):
    """
    Returns the encoded or decoded message.
    """
    rot_message = ''
    for char in message:
        if char.islower():
            letters = ascii_lowercase
        elif char.isupper():
            letters = ascii_uppercase
        else:
            # char is not a letter -- leave it unmodified
            rot_message += char
            continue

        position = letters.find(char)
        new_position = position + 13
        rot_message += letters[new_position % 26]  # mod to stay in bounds
    return rot_message


def main(args):
    """Main program code."""
    if len(args) != 1:
        print('usage: python rot13.py message')
        sys.exit(1)

    message = sys.argv[1]

    rot = rotate(message)
    print(rot)


if __name__ == '__main__':
    main(sys.argv[1:])
